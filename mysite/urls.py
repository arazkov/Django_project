from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/', include('polls.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls')),
    path('fantlab/', include('fantlab.urls')),
]
