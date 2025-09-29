from django import forms
from .models import eventModel, prayerRequestModel


class eventForm(forms.ModelForm):
    class Meta:
        model = eventModel
        fields = ['title', 'description']

class prayerRequestForm(forms.ModelForm):
    class Meta:
        model = prayerRequestModel
        fields = ['title', 'description']
