from . import views
from django.views import generic
from django.urls import path
from .models import Venue


urlpatterns = [
    path('', views.VenueList.as_view(), name='home'),
]