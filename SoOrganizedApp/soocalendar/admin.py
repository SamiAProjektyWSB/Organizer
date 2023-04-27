from django.contrib import admin
from soocalendar.models import Calendar, Event

admin.site.register(Calendar)
admin.site.register(Event)