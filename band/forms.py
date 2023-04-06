from django import forms
from django.forms import ModelForm
from .models import BandUsers, Venue, Event

class VenueForm(ModelForm):
	class Meta:
		"""This class creates the form for requesting venues.
		"""
		model = Venue
		fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
		labels = {
			'name': '',
			'address': '',
			'zip_code': '',
			'phone': '',
			'web': '',
			'email_address': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name', 'style':"width: 500px"}),			
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address of Place', 'style':"width: 500px"}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Its Zip Code', 'style':"width: 500px"}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number We Can Phone','style':"width: 500px"}),
			'web': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Website We Can Look At','style':"width: 500px"}),
			'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address We Can Contact', 'style':"width: 500px"}),

		}

class EventForm(ModelForm):
	class Meta:
		"""This class creates the form for requesting events.
		"""
		model = Event
		fields = ('name', 'event_date', 'venue')
		labels = {
			'name': '',
			'event_date': 'yyyy-mm-dd hh:mm:ss',
			'venue':'Give your event a venue',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name your event', 'style':"width: 500px"}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Give your event a date', 'style':"width: 500px"}),
			'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Give it a venue', 'style':"width: 500px"}),
		}