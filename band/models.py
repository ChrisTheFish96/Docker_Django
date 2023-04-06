from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
	"""This class creates the model for requesting venues.
	"""
	name = models.CharField(max_length = 120)
	address = models.CharField(max_length = 300)
	zip_code = models.CharField(max_length = 10)
	phone = models.CharField(max_length = 15, blank=True)
	web = models.URLField(blank=True)
	email_address = models.EmailField(blank=True)
	approved = models.BooleanField('Approved', default=False)

	def __str__(self):
		return self.name

class BandUsers(models.Model):
	"""This class creates the model for adding users.
	"""
	first_name = models.CharField(max_length = 120)
	last_name = models.CharField(max_length = 120)
	email = models.EmailField()

	def __str__(self):
		return self.first_name + ' ' + self.last_name
		
class Event(models.Model):
	"""This class creates the model for requesting events.
	"""
	name = models.CharField(max_length = 120)
	event_date = models.DateTimeField()
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
	manager = models.CharField(max_length = 60, default = 'Jack Black')
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(BandUsers, blank=True)
	approved = models.BooleanField('Approved', default=False)
	def __str__(self):
		return self.name