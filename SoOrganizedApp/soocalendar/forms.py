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
    
class EventAdd(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ()