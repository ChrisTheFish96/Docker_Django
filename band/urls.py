from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('events/', views.all_events, name='list-events'),
    path('add_venue/', views.add_venue, name = 'add_venue'),
    path('add_event/', views.add_event, name = 'add_event'),
    path('admin_approval_venues/', views.admin_approval_venues, name = 'admin_approval'),
    path('admin_approval_events/', views.admin_approval_events, name = 'admin_approval_events'),
]
