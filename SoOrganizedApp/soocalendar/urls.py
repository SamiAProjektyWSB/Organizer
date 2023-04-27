from django.contrib import admin
from django.urls import path, include
from account.views import home

urlpatterns = [
    path('home/', home, name='home')
]