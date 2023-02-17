from django import forms
from .models import Room

class AvailabilityForm(forms.Form):
    check_in = forms.DateTimeField(required=True, input_formats=['%Y-%m-%d %H:%M', ])
    check_out = forms.DateTimeField(required=True, input_formats=['%Y-%m-%d %H:%M', ])
