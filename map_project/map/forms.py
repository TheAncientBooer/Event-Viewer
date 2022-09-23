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
# form = EventForm()    
# event = Event.objects.get(pk=1)
# form = EventForm(instance=event)

    # class Meta:
    #     model = Event
    #     fields = ['title', 'description', 'location', 'start_date', 'end_date', 'website', ]