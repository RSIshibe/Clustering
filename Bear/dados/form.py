from django import forms


class EventsForm(forms.Form):
    file = forms.FileField()