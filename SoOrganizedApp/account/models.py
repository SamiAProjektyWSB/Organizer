from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from SoOrganizedApp import settings


    

class AccountsManager(BaseUserManager):
    def create_user(self, mail, nick, password):
        user = self.model(mail=mail, nick=nick, password=password)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, mail, nick, password):
        user = self.create_user(mail=mail, nick=nick, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser):
    mail = models.EmailField(verbose_name="e-mail", max_length=50, unique=True)
    nick = models.CharField(verbose_name="nick", max_length=30)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    join_date = models.DateTimeField(verbose_name="date", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last logon", auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'mail'

    REQUIRED_FIELDS = ["nick"]

    objects = AccountsManager()

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_admin