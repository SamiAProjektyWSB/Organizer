from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from account.forms import AuthForm, Registration
from soocalendar.views import home
from django.contrib import messages
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str

def Activate(request, uidb64, token):
    return redirect('home')

def activateEmail(request, user, to_mail):
    mail_topic = 'Potwierdź adres e-mail'
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    protocol = 'https' if request.is_secure() else 'http'
    domain = get_current_site(request).domain

    message = render_to_string("mail-template.html", {
        'user': user.nick,
        'domain': domain,
        'uid': uid,
        'token': token,
        'protocol': protocol
    })
    mail = EmailMessage(mail_topic, message, to={to_mail})
    if mail.send():
        messages.success(request, f'Drogi użytkowniku {user.nick} na twoją skrzynkę pocztową został wysłany mail w celu potwierdzenia tożsamości, proszę o zapoznanie się z nim.')
    
    else:
        messages.error(request, f'Błąd! Nie udało się wysłać wiadomości na podany adres mailowy')

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
            activateEmail(request, user, form.cleaned_data.get('mail'))
            return redirect('email-request')
    else:
        form = Registration()

    context['form'] = form    
    
    return render(request, "register.html", context)

def passwordRecovery(request):
    return render(request, "password-recovery.html", {})

def logoutPage(request):
    logout(request)
    return redirect("login")

def emailRequest(request):
    return render(request, "email-request.html", {})

