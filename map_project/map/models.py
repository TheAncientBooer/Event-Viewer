import json
from django.db import models

# Create your models here.


class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
class Event(models.Model):
     title = models.CharField(max_length=200, null=True)
     description = models.TextField(null=True)
     location = models.CharField(max_length=500, null=True)
     start_date = models.DateTimeField()
     end_date = models.DateTimeField()