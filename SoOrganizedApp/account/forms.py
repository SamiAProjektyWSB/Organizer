from django import forms
from django.contrib.auth.forms import UserCreationForm,  SetPasswordForm, PasswordResetForm
from django.contrib.auth import authenticate
from account.models import Account

class Registration(UserCreationForm):

    class Meta:
        model = Account
        fields = ("mail","nick","password1","password2")


class AuthForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ("mail", "password")

    def clean(self):
        if self.is_valid():
            mail = self.cleaned_data['mail']
            password = self.cleaned_data['password']

            if not authenticate(mail=mail, password=password):
                self.add_error("password", "Błędne wprowadzone hasło lub adres e-mail")
                raise forms.ValidationError("Dane niepoprawne")
            

class SetPasswordForm(SetPasswordForm):

    class Meta:
        model = Account
        fields = ("new_password1","new_password2")

class PasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
