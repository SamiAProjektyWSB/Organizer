from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from soocalendar.forms import CalendarInput, CalendarChange, addEvent
from soocalendar.serializers import Serializer, eventSerializer
from soocalendar.models import Calendar
from rest_framework.utils import json


def getEvents(calendarChosen):
    calendar = Calendar.objects.get(calendar_id=calendarChosen)
    serializedEvent = eventSerializer(calendar.event_set.all(), many=True).data
    return serializedEvent


@login_required
def home(request):
    add_event = addEvent()
    context = {}
    

    if "calendarChosen" in request.GET:
        calendarChosen = request.GET["calendarChosen"]
        firstCalendar = True
    else:
        firstCalendar = Calendar.objects.filter(owner=request.user).first()
        if firstCalendar:
            calendarChosen = firstCalendar.calendar_id


    if request.POST:
        if request.POST['action'] == 'create':
            form = CalendarInput(request.POST)
            if form.is_valid():
                form.set_owner(request.user)
                calendar = form.save(commit=False)
                calendar.owner_id = request.user.pk
                calendar.save()

        if request.POST['action'] == 'delete':
            calendar = Calendar.objects.get(calendar_id=request.POST["calendar_id"])
            if calendar.owner == request.user:
                calendar.delete()
                firstCalendar = Calendar.objects.filter(owner=request.user).first()
                if firstCalendar:
                    calendarChosen = firstCalendar.calendar_id


        if request.POST['action'] == "edit":
            form = CalendarChange(request.POST)
            if form.is_valid():
                form.save(commit=True)

        if request.POST['action'] == 'newevent':
            form = addEvent(request.POST)
            if form.is_valid():
                form.set_calendar(calendarChosen)
                form.save()
                add_event = addEvent()
            else:
                print(form)
                add_event = form


    

    queryset_accesed = Calendar.objects.filter(Q(owner=request.user.pk) | Q(visible_for=request.user))
    queryset_edit = Calendar.objects.filter(Q(owner=request.user.pk) | Q(editable_by=request.user))
    context["calendars"] =  Serializer( queryset_edit, many=True).data
    context['create'] = CalendarInput()
    context['edit'] = CalendarChange(initial={"user_id": request.user.pk, "owner": request.user})
    context['soocalendars'] = queryset_accesed

    if firstCalendar:
        context['calendarChosen'] = int(calendarChosen)
        context['events'] = getEvents(calendarChosen)
    context['addevent'] = add_event


    return render(request, "home.html", context)