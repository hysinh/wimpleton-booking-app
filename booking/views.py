from django.contrib import messages
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Venue, Booking
from .forms import BookingForm

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
     queryset = Venue.objects.filter(status=1)
     template_name = "booking/venue_list.html"
     paginate_by = 6


@login_required()
def booking_dashboard(request):
    bookings = Booking.objects.filter(client_id=request.user)
    return render(
         request, 
         'user/booking_dashboard.html',
         {'bookings': bookings}
     )


@login_required()
def request_booking(request):
     """
     Creates a booking request
     """
     if request.method == 'POST':
          form = BookingForm(request.POST)
          if form.is_valid():
               booking = form.save(commit=False)
               booking.client = request.user
               booking.save()
          
          return redirect('booking-dashboard')
     
     form = BookingForm()
     venues = Venue.objects.filter(status=1)
     context = {
          "form": form,
          "venues": venues
     }
          
     return render(request, 'user/request_booking.html', context)



@login_required()
def edit_booking(request, client, booking_id):
     """
     Edits an exiting booking related to User

     **Context**
     ``booking``
          And instance of :model:'booking.Booking'
     """
     booking = Booking.objects.filter(client=request.user)

     context = {
          "booking": booking
     }
          
     return render(request, 'user/edit_booking.html', context)


  
# Public pages
def homepage(request):
     return render(request, 'public/index.html')

def aboutpage(request):
     return render(request, 'public/about.html')

def contactpage(request):
     return render(request, 'public/contact.html')



