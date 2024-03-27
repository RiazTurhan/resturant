from django.contrib import admin
from django.urls import path
from page_sec import views

urlpatterns = [
    path('booking/', views.book),
    path('team/', views.team),
    path('test/', views.test )
]
