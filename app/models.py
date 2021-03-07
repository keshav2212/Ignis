from django.db import models
class Event(models.Model):
	Event_Name=models.CharField(max_length=100)
	Creation_Date=models.DateField()
	Creation_Time=models.TimeField()
	Location=models.CharField(max_length=50)
	Image=models.ImageField(upload_to='events')
	is_liked = models.BooleanField(default=False) 
	def __str__(self):
		return self.Event_Name
# Create your models here.
