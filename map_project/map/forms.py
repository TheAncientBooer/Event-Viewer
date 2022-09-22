from django import forms
from .models import Search, Event
class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')
    class Meta:
        model = Search
        fields = ['address']

class EventForm(forms.Form): #WAS    forms.ModelForm):
    title = forms.CharField(label='title' , max_length=200)
    description = forms.CharField(label='description')
    location = forms.CharField(label='location', max_length=500)
    start_date = forms.DateField(label='Start Date', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='End Date', widget=forms.SelectDateWidget)
    website = forms.URLField(label='Website', max_length=1000, required=False)

    # class Meta:
    #     model = Event
    #     fields = ['title', 'description', 'location', 'start_date', 'end_date', 'website', ]