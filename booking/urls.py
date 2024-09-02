from . import views
from django.views import generic
from django.urls import path
from .views import (
    view_bookings,
    list_approved_bookings
)


urlpatterns = [
    
    # public pages (no login required)
    path('', views.homepage, name='home'),
    path('about/', views.aboutpage, name='about'),
    path('contact/', views.contactpage, name='contact'),
    path('venue-hire/', views.VenueList.as_view(), name='venue-hire'),

    # registered user pages
    path('create-booking/', views.create_booking, name='create-booking'),
    path('venue-hire/', views.VenueList.as_view(), name='venue-hire'),
    path('booking-list/', view_bookings, name='booking-list'),
    path('booking-approved/', list_approved_bookings, name='approved-bookings'),
    





]

