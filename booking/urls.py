from . import views
from django.views import generic
from django.urls import path
from .models import Venue


urlpatterns = [
    # public pages (no login required)
    path('', views.homepage, name='welcome'),

    # path('', views.VenueList.as_view(), name='home'),
    path('venue-hire/', views.VenueList.as_view(), name='venue-hire'),





]

