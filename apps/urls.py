from django.urls import include, path
from . import views

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.airlines, name='airlines'),
    path('list', views.airline_list, name='search-airline'),
    path('charts', views.charts, name='charts-view'),
    path('poll', views.airline_poll ,name='airline_poll')
]