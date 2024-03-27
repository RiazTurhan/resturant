from django.contrib import admin
from django.urls import path
from serv import views

urlpatterns = [
    path('', views.service)
]