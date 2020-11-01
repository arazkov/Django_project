from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from requests import get
import requests, json

def what_city(ip):
    result = json.loads(get(f'http://ip-api.com/json/{ip}?lang=ru').text)
    return result['city']

def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 3,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'

def weather_def(request):
    time_now = dt.datetime.now().strftime('%H:%M')
    ip = get('https://api.ipify.org').text
    return render(request, 'weather/weather.html', {'ip': ip,
                                                    'time': time_now,
                                                    'city': what_city(ip),
                                                    'weather': what_weather(what_city(ip))
                                                    })
