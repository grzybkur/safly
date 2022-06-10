from django.shortcuts import render
from django.http import HttpResponse
from .apps import AppsConfig 
from .models import Airline, Delays, Vote
from datetime import datetime
import numpy as np
import random
from tensorflow import keras
#model = keras.models.load_model('model')
# Create your views here.

def airlines(request):
    # conn = 
    results = Airline.objects.all
    airline_list = Airline.objects.all()
    # suma-do-wyświetlenia = models.raw(sql_query)
    context = {
        'showname' : results,
        'airlines' : airline_list
    }
    return render(request, "apps/base.html", context)

def airline_list(request):
    results = Airline.objects.all
    if request.method == "POST":
        first_airline=request.POST['searched_airplane']
        second_airline=request.POST['searched_airplane_second']
        if(first_airline == ""):
            first_airline = second_airline
        elif(second_airline == ""):
            second_airline = first_airline
        if(first_airline and second_airline):
            print("request got right values")
            left_airline = Airline.objects.filter(dfop_carrier=first_airline)
            right_airline = Airline.objects.filter(dfop_carrier=second_airline)

            first_plot_data = Delays.objects.filter(dfop_carrier=first_airline)
            first_plot_data = [{'x' : datetime.strptime(str(record.dfyear)+str(record.dfmonth),'%Y%m'), 'y' : record.dfnumofdelay} for record in first_plot_data]
            first_plot_data.sort(key=lambda x: x['x'])

            second_plot_data = Delays.objects.filter(dfop_carrier=second_airline)
            second_plot_data = [{'x' : datetime.strptime(str(record.dfyear)+str(record.dfmonth),'%Y%m'), 'y' : record.dfnumofdelay} for record in second_plot_data]
            second_plot_data.sort(key=lambda x: x['x'])
            #model = keras.models.load_model('model')
            one = [i for i in left_airline.values()]
            two = [i for i in right_airline.values()]
            modelInput = np.array([one[0]['amount_of_delays'],two[0]['amount_of_delays'],one[0]['amount_of_flights'],two[0]['amount_of_flights'],one[0]['chance_of_accident'],two[0]['chance_of_accident'],one[0]['chance_of_delay'],two[0]['chance_of_delay'],one[0]['mean_of_delay'],two[0]['mean_of_delay'],one[0]['number_of_accidents'],two[0]['number_of_accidents']]).reshape(1,-1)
            modelInput = modelInput.astype(float)

            model_result = AppsConfig.model.predict(modelInput)[0,0]
            model_choice = one[0]['dfop_carrier']
            if(model_result == 1):
                model_choice = one[0]['dfop_carrier']
            else:
                model_choice = two[0]['dfop_carrier']
            
            context = {
                'first_airline' : left_airline.values(),
                'second_airline' : right_airline.values(),
                'showname' : results,
                'first_plot': first_plot_data,
                'second_plot' : second_plot_data,
                'model_choice' : model_choice,
                'model_result' : model_result
            }
            print(first_airline)
        return render(request, "apps/airline_list.html", context=context)

    else:
        return render(request, "apps/airline_list.html", context={})

def airline_poll(request):
    results = Airline.objects.all
    items = list(Airline.objects.all())
    tmp = ['AQ','FL','AS','G4','AA','EV','OH','CO','DL','XE','9E','MQ','F9','HA','QX','B6','YV','NW','YX','OO','WN','NK','UA','US','VX']
    random_items = random.sample(tmp, 2)
    left_airline = Airline.objects.filter(carrier=random_items[0])
    right_airline = Airline.objects.filter(carrier=random_items[1])
    context = {
        'showname' : results,
        'first_airline' : left_airline.values(),
        'second_airline' : right_airline.values()
    }

    user_vote = 1
    if request.method == "POST":
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            user_vote = 1
        elif selected_option == 'option2':
            user_vote = 2
        else:
            return HttpResponse(400, 'Invalid form')
        
        v = Vote(carrier_1 = request.POST['first_airline_dfop_carrier'],
                amount_of_delays_1=request.POST['first_airline_amount_of_delays'],
                amount_of_flights_1=request.POST['first_airline_amount_of_flights'],
                mean_of_delay_1 = request.POST['first_airline_mean_of_delay'],
                number_of_accidents_1 = request.POST['first_airline_number_of_accidents'],
                chance_of_delay_1 = request.POST['first_airline_chance_of_delay'],
                chance_of_accident_1 = request.POST['first_airline_chance_of_accident'],
                carrier_2 = request.POST['second_airline_dfop_carrier'],
                amount_of_delays_2=request.POST['second_airline_amount_of_delays'],
                amount_of_flights_2=request.POST['second_airline_amount_of_flights'],
                mean_of_delay_2 = request.POST['second_airline_mean_of_delay'],
                number_of_accidents_2 = request.POST['second_airline_number_of_accidents'],
                chance_of_delay_2 = request.POST['second_airline_chance_of_delay'],
                chance_of_accident_2 = request.POST['second_airline_chance_of_accident'],
                user_choice = user_vote)
        v.save()

    return render(request, "apps/airline_poll.html", context=context)


def charts(request):
    airline_name='Endeavor Air'
    airline_chart = Delays.objects.filter(dfop_carrier=airline_name)
    airline_chart = [{'x' : datetime.strptime(str(record.dfyear)+str(record.dfmonth),'%Y%m'), 'y' : record.dfnumofdelay} for record in airline_chart]
    print(airline_chart)
    context = {
        'data' : airline_chart
    }
    return render(request, "apps/charts.html", context=context)

