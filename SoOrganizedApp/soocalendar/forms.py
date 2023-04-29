from django import forms
from soocalendar.models import Calendar, Event
from account.models import Account

class CalendarInput(forms.ModelForm):
    visible_for = forms.CharField(required=False)
    editable_by = forms.CharField(required=False)


    class Meta:
        model = Calendar
        exclude=("owner", "visible_for","editable_by")

    def save(self, commit=True):
        calendar = self.instance
        for mail in self.cleaned_data["visible_for"].split(";"):
            if Account.objects.filter(mail=mail).exists():
                calendar.visible_for.add(mail)

        for mail in self.cleaned_data["editable_by"].split(";"):
            if Account.objects.filter(mail=mail).exists():
                calendar.editable_by.add(mail)

        if commit:
            calendar.save()

        return calendar
    
    def set_owner(self, user):
        calendar = self.instance
        calendar.owner_id = user.pk
        self.instance = calendar
class addEvent(forms.ModelForm):

    beggining_date = forms.DateTimeField(input_formats=["$d.%m.%Y %H:%M"], required=True)
    end_time = forms.DateTimeField(input_formats=["$d.%m.%Y %H:%M"], required=False)

    def set_calendar(self, calendar_id):
        event = self.instance
        event.calendar_id = calendar_id
        self.instance = event


    class Meta:
        model = Event
        exclude = ('calendar',)

def get_calendar(user_id):
    calendars = Calendar.objects.filter(owner=user_id)
    choices = []

    for calendar in calendars:
       choices.append((calendar.pk, calendar.name))

    return choices

class CalendarChange(forms.ModelForm):
    calendar_id = forms.CharField(required=True)
    editable_by = forms.CharField(required=False)
    visible_for = forms.CharField(required=False)

    class Meta:
        model = Calendar
        exclude = ("visible_for", "editable_by")  

    def __init__(self, *args, **kwargs):
        super(CalendarChange, self).__init__(*args, **kwargs)
        if self.initial:
            self.fields["calendars"] = forms.ChoiceField(choices=get_calendar(self.initial["user_id"]), required=True)
    
    def save(self, commit=True):
        calendar = Calendar.objects.get(calendar_id=self.cleaned_data["calendar_id"])
        calendar.name = self.cleaned_data["name"]
        calendar.editable_by.clear()
        calendar.visible_for.clear()

        for mail in self.cleaned_data["visible_for"].split(";"):
            if Account.objects.filter(mail=mail).exists():
                calendar.visible_for.add(mail)

        for mail in self.cleaned_data["editable_by"].split(";"):
            if Account.objects.filter(mail=mail).exists():
                calendar.editable_by.add(mail)

        if commit:
            calendar.save()

        return calendar
    

