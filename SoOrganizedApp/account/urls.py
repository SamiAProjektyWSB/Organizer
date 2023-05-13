from django.contrib import admin
from django.urls import path, include
from account.views import loginPage, register, passwordRecovery, logoutPage, emailRequest, Activate, changepass, password_reset_request

urlpatterns = [
    path('login/', loginPage, name="login"),
    path('register/', register, name="register"),
    path('passrec/', passwordRecovery, name="passrec"),
    path('logout/', logoutPage, name="logout"),
    path('info/', emailRequest, name="email-request"),
    path('activate/<uidb64>/<token>', Activate, name="activate"),
    path('changepass/', changepass, name="changepass"),
    path('reset/<uidb64>/<token>', password_reset_request, name="reset"),
]
