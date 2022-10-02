from django.db import models 

class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
        
class Event(models.Model):
     title = models.CharField(max_length=200, null=True)
     description = models.TextField(null=True)
     address = models.CharField(max_length=500, null=True)
     start_date = models.DateField() 
     end_date = models.DateField()

    #  def event_location(self):
    #         return self.event_location
    
     def __str__(self):
            return self.title  