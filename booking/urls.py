from . import views
from django.views import generic
from django.urls import path
from .views import venue_detail


urlpatterns = [
    
    # public pages (no login required)
    path('', views.homepage, name='home'),
    path('about/', views.aboutpage, name='about'),
    path('contact/', views.contactpage, name='contact'),
    path('venue-hire/', views.VenueList.as_view(), name='venue-hire'),

    # registered user pages
    path('add-booking/', views.add_booking, name='add-booking'),
    path('venue-hire/', views.VenueList.as_view(), name='venue-hire'),
    path('booking-list/', views.BookingList.as_view(), name='booking-list'),
    path('booking-approved/', views.list_approved_bookings, name='approved-bookings'),
    





]

