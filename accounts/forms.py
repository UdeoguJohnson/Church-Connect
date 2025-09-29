from django import forms
from .models import churchModel
from core.models import userModel

class registerChurchForm(forms.ModelForm):
    class Meta:
        model = churchModel
        fields = ['name', 'location']


class signUpForm(forms.ModelForm):
    class Meta:
        model = userModel
        fields = ['first_name', 'last_name', 'email']
