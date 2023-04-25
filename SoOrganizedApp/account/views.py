from django.shortcuts import render

def login(request):
    return render(request, "login.html", {})

def register(request):
    return render(request, "register.html", {})

def passwordRecovery(request):
    return render(request, "password-recovery.html", {})

def home(request):
    return render(request, "base.html", {})

