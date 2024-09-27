from . import views
from django.views import generic
from django.urls import path
from .views import booking_dashboard
from django.conf.urls import handler403, handler404, handler500
from .views import display_404, display_500


# 404 and 500 custom error pages
handler404 = display_404
handler500 = display_500


urlpatterns = [
    # public pages (no login required)
    path('', views.homepage, name='home'),
    path('about/', views.aboutpage, name='about'),
    path('contact/', views.contactpage, name='contact'),
    path('venue-hire/', views.VenueList.as_view(), name='venue-hire'),

    # registered user pages
    path('edit-booking/<int:booking_id>/',
         views.edit_booking, name='edit-booking'),
    path('delete-booking/<int:booking_id>/',
         views.delete_booking, name='delete-booking'),
    path('request-booking/', views.request_booking, name='request-booking'),
    path('request-booking-test/', views.request_booking_test,
         name='request-booking-test'),
    path('venue-hire/', views.VenueList.as_view(), name='venue-hire'),
    path('booking-dashboard/', booking_dashboard, name='booking-dashboard'),
]
