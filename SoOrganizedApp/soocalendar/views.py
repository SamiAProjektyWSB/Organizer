from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from soocalendar.forms import CalendarInput

@login_required
def home(request):
    context = {

    }
    if request.POST:
        form == CalendarInput(request.POST)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.owner_id = request.user.pk
            calendar.save()


    form = CalendarInput()
    context["form"] = form
    return render(request, "home.html", {})