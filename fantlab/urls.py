from django.urls import path
from . import views

app_name = 'fantlab'

urlpatterns = [
    # fanflab/
    path('', views.fantlab_index, name='fantlab_index')
] 
