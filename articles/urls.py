from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    # articles/
    path('', views.index, name='index'),
    # articles/1/
    path('<int:article_id>/', views.detail, name='detail'),
    # articles/1/leave_comment/
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    ]