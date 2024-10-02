from django.test import TestCase
from .models import Booking, Contact, Venue
from .forms import BookingForm, ContactForm
from django.contrib.auth.models import User
from django.urls import reverse
import json

# Create your tests here.
class TestBlogViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testUser",
            password="Password",
            email="test@test.com"
        )

        chapel: Venue = Venue(
            venue_name="The Chapel",
            venue_capacity=5,
            staff_member=self.user
        )
        chapel.save()
        
        self.booking = Booking(
            venue=chapel.id,
            client=self.user,
            event_type="Wedding",
            event_date="2024-09-18",
            num_guests=200,
        )
        self.booking.save()

    def test_render_booking_dashboard(self):
        """
        Tests that the booking dashboard renders correctly
        """
        response - self.client.get(reverse(
            'booking', args=['booking_id']))
        print(response.context)
        self.assertEqual(response.status_code, 200)