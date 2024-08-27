from django.shortcuts import render, get_object_or_404
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
     #model = Venue
     queryset = Venue.objects.filter(status=1)
     template_name = "booking/venue_list.html"
     paginate_by = 6


def venue_detail(request,slug):
     """
     Display an individual :model: 'booking.Venue'
     ** Context **
     "venue"
      an instance of :model: 'booking.Venue'
     ** Template **
     : template: 'booking/venue_detail.html'
     """

     queryset = Venue.objects.filter(status=1)
     venue = get_object_or_404(queryset, slug=slug)

     return render (
          request,
          'booking/venue_detail.html',
          {"booking":venue},
     )


def booking_form(request, slug):
     """
     Displays the booking form :model: 'booking.Booking'
     """
     model = booking_form
     template_name = "booking/booking_form.html"


# Public pages

def homepage(request):
    return render(request, 'booking/index.html')
