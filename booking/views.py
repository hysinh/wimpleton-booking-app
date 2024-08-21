from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Venue

# Create your views here.
class VenueList(generic.ListView):
     """
     Renders a paginated view of 6 posts the queryset displaying the title and
     basic information about each venue allowing user to navigate view all venue
     options.
     Displays an multiple descending instances of :model:`booking.Venue`.
     **Context**
     ``index``
        The most recent 6 instances instance of :model:`booking.Venue`.
     **Template:**
     :template:`blog/venue_list.html`
     """
     model = Venue
     template_name = "booking/venue_list.html"
     paginate_by = 6


