from django import forms
from .models import TravelType, Trip, Questions

class TravelTypeForm(forms.ModelForm):
    class Meta:
        model=TravelType
        fields='__all__'

class TripForm(forms.ModelForm):
    class Meta:
        model=Trip
        fields='__all__'

class QuestionsForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields='__all__'        
