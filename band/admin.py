from django.contrib import admin
from . models import Venue, BandUsers, Event

admin.site.register(BandUsers)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	"""This class creates a model to which the venue admin section is created.
	"""
	list_display = ('name', 'address', 'email_address')
	ordering=('name',)
	search_fields = ('name', 'zip_code')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	"""This class creates a model to which the event admin section is created.
	"""
	fields = (('name', 'venue'), 'event_date', 'description', 'manager', 'approved')
	list_display = ('name','event_date', 'venue')
	list_filter = ('event_date', 'venue')
	ordering = ('-event_date',)
