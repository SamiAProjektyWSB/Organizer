from django.contrib import admin
from django.urls import path, include
from account.views import login, register, passwordRecovery

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('passrec/', passwordRecovery, name="passrec"),
]
