from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

def weather_def(request):
    time_now = dt.datetime.now().strftime('%H:%M')
    return HttpResponse('Weather page\ntime now {}'.format(time_now))

