from . import views
from django.urls import path
from .views import booking_dashboard, display_404, display_500


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
    path('venue-hire/', views.VenueList.as_view(), name='venue-hire'),
    path('booking-dashboard/', booking_dashboard, name='booking-dashboard'),
]
