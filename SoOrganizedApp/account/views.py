from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from account.forms import AuthForm, Registration
from soocalendar.views import home

def loginPage(request):
    context = {}
    if request.POST:
        form = AuthForm(request.POST)
        if form.is_valid():
            mail = request.POST['mail']
            password = request.POST['password']
            user = authenticate(mail=mail, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = AuthForm()

    context['form'] = form
        
    return render(request, "login.html", context)

def register(request):
    context = {}
    if request.POST:
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = Registration()

    context['form'] = form    
    
    return render(request, "register.html", context)

def passwordRecovery(request):
    return render(request, "password-recovery.html", {})

def logoutPage(request):
    logout(request)
    return redirect("login")


