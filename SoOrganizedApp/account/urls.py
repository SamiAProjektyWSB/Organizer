from django.contrib import admin
from django.urls import path, include
from account.views import loginPage, register, passwordRecovery, home, logoutPage

urlpatterns = [
    path("", home, name="home"),
    path('login/', loginPage, name="login"),
    path('register/', register, name="register"),
    path('passrec/', passwordRecovery, name="passrec"),
    path('logout/', logoutPage, name="logout"),
]
