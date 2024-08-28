from . import views
from django.views import generic
from django.urls import path
from .views import venue_detail


urlpatterns = [
    # public pages (no login required)
    path('', views.homepage, name='home'),
    # path('', views.VenueList.as_view(), name='home'),
    path('venue-hire/', views.VenueList.as_view(), name='venue-hire'),
    path('booking-list/', views.BookingList.as_view(), name='booking-list'),
    path('venue-detail', venue_detail),
    path('booking-approved/', views.list_approved_bookings, name='approved-bookings'),
    





]

