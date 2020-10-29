from django.shortcuts import render
from django.http import HttpResponse

def weather_def(request):
    return HttpResponse('Weather page')

