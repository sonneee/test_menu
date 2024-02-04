from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('index', views.menu, name='menu'),
    path('index2', views.menu, name='menu'),
    path('index0', views.menu, name='menu'),
    path('index3', views.menu, name='menu'),
    ]