from django.shortcuts import render 
from .models import User, Event
from django.http import HttpResponse, HttpResponseRedirect



def index(request):
    return render(request, 'index.html')