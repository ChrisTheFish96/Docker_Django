from django.shortcuts import render
from .models import Event, Venue
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect
from django.contrib import messages

	
def admin_approval_venues(request):
	"""This method will be used by admins to approve venues
		:returns: Redirects to home page with success message if successful
		:rtype: URL redirection
	"""
	venue_list = Venue.objects.all()
	if request.user.is_superuser:
		if request.method=="POST":
			id_list = request.POST.getlist('boxes')
			# Uncheck everything.
			venue_list.update(approved=False)

			#Updating the database.
			for x in id_list:
				Venue.objects.filter(pk=int(x)).update(approved=True)

			messages.success(request, "Venue list approval updated.")
			return render(request, 'band/home.html', {})	

		else:
			return render(request, 'band/admin_approval_venues.html', {'venue_list':venue_list})
	else:
		messages.success(request, "You aren't authorized to view this page.")
		return render(request, 'band/home.html', {})
	return render(request, 'band/admin_approval_venues.html', {})

def admin_approval_events(request):
	"""This method will be used by admins to approve events
		:returns: Redirects to home page with success message if successful
		:rtype: URL redirection
	"""
	event_list = Event.objects.all(). order_by('-event_date')
	if request.user.is_superuser:
		if request.method=="POST":
			id_list = request.POST.getlist('boxes')
			# Uncheck everything.
			event_list.update(approved=False)

			#Updating the database.
			for x in id_list:
				Event.objects.filter(pk=int(x)).update(approved=True)

			messages.success(request, "Event list approval updated.")
			return render(request, 'band/home.html', {})	

		else:
			return render(request, 'band/admin_approval_events.html', {'event_list':event_list})
	else:
		messages.success(request, "You aren't authorized to view this page.")
		return render(request, 'band/home.html', {})
	return render(request, 'band/admin_approval_events.html', {})	

def home(request):
	"""This method will be used to return to home screen
	"""
	return render(request, 'band/home.html', {})

def all_events(request):
	"""This method will be used to view all approved events
		:returns: Redirects to events page
		:rtype: URL redirection
	"""
	event_list = Event.objects.all()
	return render(request, 'band/event_list.html', {'event_list':event_list})

def all_venues(request):
	"""This method will be used to view all approved venues
		:returns: Redirects to venue page
		:rtype: URL redirection
	"""
	venue_list = Venue.objects.all()
	return render(request, 'band/venue_list.html', {'event_list':event_list})

def add_event(request):
	"""This method will be used to request new events
		:returns: Redirects to home page with success message if successful
		:rtype: URL redirection
	"""
	submitted = False
	if request.method == "POST":
		event_form = EventForm(request.POST)
		if event_form.is_valid() :
			event_form.save()
			messages.success(request, ("Request succesfully sent."))
			return render(request, 'band/home.html')
	else:
		event_form = EventForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'band/add_event.html', {'event_form':event_form, 'submitted':submitted})

def add_venue(request):
	"""This method will be used to request new venues
		:returns: Redirects to home page with success message if successful
		:rtype: URL redirection
	"""
	submitted = False
	if request.method == "POST":
		venue_form = VenueForm(request.POST)
		if venue_form.is_valid():
			venue_form.save()
			messages.success(request, ("Request succesfully sent."))
			return render(request, 'band/home.html')
	else:
		venue_form = VenueForm
		if 'submitted' in request.GET:
			submitted = True
		return render(request, 'band/add_venue.html', {'venue_form': venue_form, 'submitted':submitted})

