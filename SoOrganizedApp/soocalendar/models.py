from django.db import models
from account.models import Account

class Calendar(models.Model):
    calendar_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    visible_for = models.ManyToManyField(Account, related_name="visible_for")
    editable_by = models.ManyToManyField(Account, related_name="editable_by")

    def __str__(self):
        return self.name
    

class Event(models.Model):


    CHOICE = [
        ("P", "Praca"),
        ("D", "Obowiązki domowe"),
        ("O", "Sprawy osobiste"),
        ("S", "Spotkanie"),
    ]

    event_id = models.AutoField(primary_key=True)
    calendar_id = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    event_type =  models.CharField(max_length=1 , choices=CHOICE, default="P")

    def __str__(self):
        return self.name
    


