import datetime

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
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
     #model = Venue
     queryset = Venue.objects.filter(status=1)
     template_name = "booking/venue_list.html"
     paginate_by = 6



# class BookingList(generic.ListView):
#      """
#      Displays all the instances of Booking :model: 'booking.Booking'
#      """
#      #model = Booking
#      queryset = Booking.objects.all()
#      template_name = "booking/booking_list.html"


@login_required()
def booking_dashboard(request):
    bookings = Booking.objects.all()
    return render(
         request, 
         'user/booking_dashboard.html',
         {'bookings': bookings}
     )


# @login_required()
# def create_booking(request):
#      """
#      Creates a new booking
#      """
#      # if this is a POST request then process the Form data
#      # 'venue',
#           #   'event_type',
#           #   'event_date',
#           #   'num_guests'
#      if request.method == 'POST':
#           venue = request.POST.get('venue')
#           event_type = request.POST.get('event_type')
#           event_date = request.POST.get('event_date')
#           num_guests = request.POST.get('num_guests')
          # event_date = request.POST.get("date")

          # venue = Booking.objects.get(pk=venue)

          # user = request.user
          # booking = Booking.objects.create(
          #      client_id = user,
          #      venue=venue,
          #      event_type = event_type,
          #      event_date = event_date,
          #      num_guests = num_guests
          # )


@login_required()
def create_booking(request):
     """
     Creates a new booking
     """
     form = BookingForm()
     if request.method == 'POST':
          form = BookingForm(request.POST, request.FILES)
          if form.is_valid:
               form.instance.user = request.user
               form.save()
               messages.success(request, "Booking added successfully")
               return redirect('booking-dashboard')
 
     context = {
          'form': form
     }
     return render(request, 'user/create_booking.html', context)
     
# Public pages
def homepage(request):
     return render(request, 'public/index.html')

def aboutpage(request):
     return render(request, 'public/about.html')

def contactpage(request):
     return render(request, 'public/contact.html')



# def venue_detail(request,slug):
#      """
#      Display an individual :model: 'booking.Venue'
#      ** Context **
#      "venue"
#       an instance of :model: 'booking.Venue'
#      ** Template **
#      : template: 'booking/venue_detail.html'
#      """

#      queryset = Venue.objects.filter(status=1)
#      venue = get_object_or_404(queryset, slug=slug)

#      return render (
#           request,
#           'booking/venue_detail.html',
#           {"booking":venue},
#      )






# def add_booking(request):
#      if request.method == 'POST':
#           booking_form = BookingForm(request.POST)
#           if booking_form.is_valid:
#                booking_form.save()
#      form = BookingForm()
#      context = {
#           'booking_form': booking_form
#      }
#      return render(request, 'booking/booking_form.html', context)



