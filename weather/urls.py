from django.urls import path

from . import views

app_name = 'weather'
urlpatterns = [
    # weather/
    path('', views.weather_def, name='weather')
]