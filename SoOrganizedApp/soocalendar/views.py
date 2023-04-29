from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from soocalendar.forms import CalendarInput, CalendarChange, addEvent
from soocalendar.serializers import Serializer
from soocalendar.models import Calendar
from rest_framework.utils import json

@login_required
def home(request):
    add_event = addEvent()
    context = {}
    

    if "calendarChosen" in request.GET:
        calendarChosen = request.GET["selected_calendar"]
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
                add_event = form


    

    queryset = Calendar.objects.filter(owner=request.user.pk)
    context["calendars"] =  Serializer(queryset, many=True).data
    context['create'] = CalendarInput()
    context['edit'] = CalendarChange(initial={"user_id": request.user.pk, "owner": request.user})
    context['addevent'] = add_event
    context['soocalendars'] = queryset
    context['calendarChosen'] = int(calendarChosen)


    return render(request, "home.html", context)