from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.indexView.as_view(), name= 'index'),
    path('add', views.add, name='add')
]
