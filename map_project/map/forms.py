from django import forms
from .models import Search, Event




class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')

    class Meta:
        model = Search
        fields = ['address', ]

class EventForm(forms.ModelForm):
    title = forms.CharField(label='')
    description = forms.CharField(label='')
    location = forms.CharField(label='')
    start_date = forms.DateField(label='')
    end_date = forms.DateField(label='')
    website = forms.URLField(label='')

    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'start_date', 'end_date', 'website', ]