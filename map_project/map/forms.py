from django import forms
from .models import Search, Event
from django.forms import ModelForm
class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')
    class Meta:
        model = Search
        fields = ['address']

class EventForm(ModelForm): #WAS    forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
