from django.test import TestCase
from .models import Booking, Email
from .forms import BookingForm, EmailForm

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
        """
        data = {
            "venue": 1,
            "event_type": "Gala",
            "event_date": "2024-09-18",
            "num_guests": "200",
            "client": 1,
        }
        form = BookingForm(data=data)
        self.assertTrue(form.is_valid()) 