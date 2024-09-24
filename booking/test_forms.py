from django.test import TestCase
from .models import Booking, Email, Venue
from .forms import BookingForm, EmailForm
from django.contrib.auth.models import User
import json

# Create your tests here.
class TestEmailForm(TestCase):
    """
    Test cases for the email form
    """
    def test_email_form_is_valid(self):
        """
        Test the Email contact form with valid data
        """
        data = {
            "name": 'Ralph Test',
            "email": "test@test.com",
            "message": "Hello, This is a test",
        }
        form = EmailForm(data=data)
        self.assertTrue(form.is_valid())


class TestBookingForm(TestCase):
    """
    Test cases for the Booking form
    """
    def test_booking_form_is_valid(self):
        """
        Test the Booking form with valid data
        A portion of this test was writting by Jason Holt Smith
        """
        user: User = User()
        user.save()
        chapel: Venue = Venue(
            venue_name="The Chapel",
            venue_capacity=5,
            staff_member=user
        )
        chapel.save()
        data = {
            "venue": chapel.id,
            "event_type": "Wedding",
            "event_date": "2024-09-18",
            "num_guests": 350,
            "client": 1,
        }
        form = BookingForm(data=data)
        self.assertTrue(form.is_valid(), json.dumps(form.errors))