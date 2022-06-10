from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.

class Delays(models.Model): #class for delays chart generation
    id = models.IntegerField(primary_key=True)
    dfyear = models.IntegerField(blank=True, null=True)
    dfmonth = models.IntegerField(blank=True, null=True)
    carrier = models.CharField(max_length=2, blank=True, null=True)
    dfop_carrier = models.CharField(max_length=300, blank=True, null=True)
    dfmeantimeofdelay = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dfdelaypercent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dfnumofflights = models.IntegerField(blank=True, null=True)
    dfnumofdelay = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delays'


class Airline(models.Model):
    carrier = models.CharField(primary_key=True, max_length=2)
    dfop_carrier = models.CharField(max_length=300)
    amount_of_delays=models.IntegerField()
    amount_of_flights=models.IntegerField()
    mean_of_delay = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_flights=models.IntegerField()
    number_of_accidents=models.IntegerField()
    chance_of_delay = models.DecimalField(max_digits=5, decimal_places=2)
    chance_of_accident = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        managed = False
        db_table = 'widok_lot_final'

class Vote(models.Model):
    carrier_1 = models.CharField(max_length=300)
    amount_of_delays_1=models.IntegerField()
    amount_of_flights_1=models.IntegerField()
    mean_of_delay_1 = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_accidents_1=models.IntegerField()
    chance_of_delay_1 = models.DecimalField(max_digits=5, decimal_places=2)
    chance_of_accident_1 = models.DecimalField(max_digits=5, decimal_places=2)
    carrier_2 = models.CharField(max_length=300)
    amount_of_delays_2=models.IntegerField()
    amount_of_flights_2=models.IntegerField()
    mean_of_delay_2 = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_accidents_2=models.IntegerField()
    chance_of_delay_2 = models.DecimalField(max_digits=5, decimal_places=2)
    chance_of_accident_2 = models.DecimalField(max_digits=5, decimal_places=2)
    user_choice = models.IntegerField()