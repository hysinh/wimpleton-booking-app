from django.contrib import messages
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.core import serializers
from django.http import JsonResponse
from datetime import datetime
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
    pending_bookings = Booking.objects.filter(client_id=request.user, status=0)
    approved_bookings = Booking.objects.filter(client_id=request.user, status=1)

    context = {
          'pending_bookings': pending_bookings,
          'approved_bookings': approved_bookings,
     }
    return render(
         request, 
         'user/booking_dashboard.html',
         context
     )


@login_required()
def request_booking_test(request, id):
     """
     Creates a booking request
     """

     # get the venue 
     venue = get_object_or_404(Venue, pk=id)
     form = BookingForm(initial={"id": id})
     #contact_form = ContactForm(initial={"id": id})
     # context = {}
     # if request.method == 'POST':
     #      form = BookingForm(request.POST)
     #      if form.is_valid():
     #           booking = form.save(commit=False)
     #           already_booked_with_venue = Booking.objects.filter(venue=booking.venue, event_date=booking.event_date)
     #           if already_booked_with_venue:
     #                context = {
     #                     "form": form,
     #                     "venues": venues,
     #                     "bookings": bookings
     #                }

     #                return render(request, 'user/request_booking_test.html', context)

     #           else:
     #                booking.client = request.user
     #                booking.save()

     #                messages.success(request, "Request for a Venue booking has been created successfully.")
     #                return redirect('booking-dashboard')
     
     
     # venues = Venue.objects.filter(status=1)
     context = {
          "form": form,
          "venue": venue
          # "venue": venue,
          # "bookings": bookings
     }
          
     return render(request, 'user/request_booking_test.html', context)


@login_required()
def request_booking(request):
     """
     Creates a booking request
     """
     form = BookingForm()
     context = {}
     if request.method == 'POST':
          form = BookingForm(request.POST)
          if form.is_valid():
               booking = form.save(commit=False)
               
               # find all bookings that have the same venue and event date as selected
               # checks to see if there is already a booking with the same venue and date
               already_booked_with_venue = Booking.objects.filter(venue=booking.venue, event_date=booking.event_date)
               if already_booked_with_venue:
                    context = {
                         "form": form
                    }

                    return render(request, 'user/request_booking.html', context)

               else:
                    booking.client = request.user
                    booking.save()

                    messages.success(request, "Request for a Venue booking has been created successfully.")
                    return redirect('booking-dashboard')
     
     
     venues = Venue.objects.filter(status=1)
     context = {
          "form": form,
     }
          
     return render(request, 'user/request_booking.html', context)



@login_required()
def edit_booking(request, booking_id):
     """
     Edits an exiting booking related to User

     **Context**
     ``booking``
          An instance of :model:'booking.Booking'
     ``booking_form``
          An instance of :form:`booking.BookingForm`

     """
     # original_booking = Booking.objects.get(pk=booking_id)
     original_booking = get_object_or_404(Booking, pk=booking_id)
     
     # redirects the user back to the booking dashboard if they do not have 
     # permissions to edit the booking
     if original_booking.client != request.user: 
          messages.error(
               request, "You do not have permissions to edit this booking."
          )
          return redirect('booking-dashboard')
     
     if request.method == 'POST':
          form = BookingForm(request.POST, instance=original_booking)
          if form.is_valid():
               form.save()
               messages.success(request, "Booking edited successfully")
               return redirect('booking-dashboard')
          else:
            messages.error(
               request, "That Venue is not available for that date."
               )
     
     form = BookingForm(instance=original_booking)

     context = {
          "form": form,
          "original_booking": original_booking
     } 

     return render(request, 'user/edit_booking.html', context)   


@login_required()
def delete_booking(request, booking_id):
     """
     Delete an individual booking

     **Context**
     ``booking``
          An instance of :model:'booking.Booking'
     """
     queryset = Booking.objects.all()
     booking = get_object_or_404(queryset, pk=booking_id)
     if booking.client == request.user: 
          booking.delete()
          messages.success(request, "Booking deleted successfully")
          return redirect('booking-dashboard')
     else:
          messages.error(
               request, "You do not have permissions to delete this booking."
               )

     return HttpResponseRedirect(reverse('booking-dashboard'))



# Public pages
def homepage(request):
     return render(request, 'public/index.html')

def aboutpage(request):
     return render(request, 'public/about.html')

def contactpage(request):
     return render(request, 'public/contact.html')



