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
    bookings = Booking.objects.filter(client_id=request.user)
    return render(
         request, 
         'user/booking_dashboard.html',
         {'bookings': bookings}
     )


@login_required()
def request_booking_test(request):
     """
     Creates a booking request
     """
     bookings = Booking.objects.all()
     venues = Venue.objects.filter(status=1)
     if request.method == 'POST':
          form = BookingForm(request.POST)
          event_date = request.POST.get("event_date")
          event_date_object = datetime.strptime(event_date, "%Y-%m-%d").date()
          selected_venue = request.POST.get("venue")
          venue = get_object_or_404(Venue, pk=selected_venue)
          bookings_with_venue = Booking.objects.filter(venue=selected_venue)

          # Creates a json file of the data objects
          # data = serializers.serialize('json', bookings_with_venue)
          # return JsonResponse(data, safe=False)

          # Prints the object values
          # messages.success(
          #      request,
          #      len(bookings_with_venue)
          #      # venue.id
          # )

          # return redirect('request-booking-test')

          for booking in bookings_with_venue:
               if booking.event_date == event_date_object:
                    messages.success(
                         request,
                         "This venue date is not free! Please choose a different date for this venue."
                         # booking.event_date
                    )

                    return redirect('request-booking-test')
               
          else:
               if form.is_valid():
                    booking = form.save(commit=False)
                    booking.client = request.user
                    booking.save()

                    messages.success(request, "Request for a Venue booking has been created successfully.")
                    return redirect('booking-dashboard')
                    
               else:
                    messages.error(
                         request, "There is an error in the form. Please try again."
                         )

                    return redirect('request-booking-test')
       
     
     form = BookingForm()
     venues = Venue.objects.filter(status=1)
     context = {
          "form": form,
          "venues": venues,
          "bookings": bookings
     }
          
     return render(request, 'user/request_booking_test.html', context)


@login_required()
def request_booking(request):
     """
     Creates a booking request
     """
     bookings = Booking.objects.all()
     venues = Venue.objects.filter(status=1)
     if request.method == 'POST':
          form = BookingForm(request.POST)
          event_date = request.POST.get("event_date")
          num_guests = int(request.POST.get("num_guests"))
          event_date_object = datetime.strptime(event_date, "%Y-%m-%d").date()
          selected_venue = request.POST.get("venue")
          # venue = get_object_or_404(Venue, pk=selected_venue)
          # gets all the bookings with the matching venue
          bookings_with_venue = Booking.objects.filter(venue=selected_venue)
          for booking in bookings_with_venue:
               if booking.event_date == event_date_object:
                    messages.success(
                         request,
                         "This venue date is not free! Please choose a different date for this venue."
                    )

                    return redirect('request-booking')

          # checks guests count doesn't exceed maximum     
          if num_guests > 500:
               messages.error(
                    request, "Maximum guest count exceeded. Please change your guest count"
               )

               return redirect('request-booking')

          # checks guests count meets mimimum guest count   
          if num_guests < 20:
               messages.error(
                    request, "Booking requests require a minimum of 20 guests. Please change your guest count"
               )

               return redirect('request-booking')
               
          else:
               if form.is_valid():
                    booking = form.save(commit=False)
                    booking.client = request.user
                    booking.save()

                    messages.success(request, "Request for a Venue booking has been created successfully.")
                    return redirect('booking-dashboard')
                    
               else:
                    messages.error(
                         request, "There is an error in the form. Please try again."
                         )

                    return redirect('request-booking')
       
     
     form = BookingForm()
     venues = Venue.objects.filter(status=1)
     context = {
          "form": form,
          "venues": venues,
          "bookings": bookings
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



