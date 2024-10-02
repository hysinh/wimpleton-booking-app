from django.test import TestCase
from .models import Venue
from .forms import BookingForm, ContactForm
from django.contrib.auth.models import User
import json


# Create your tests here.
class TestContactForm(TestCase):
    """
    Test cases for the Contact form
    """
    def test_Contact_form_is_valid(self):
        """
        Test the Contact form with valid data
        """
        data = {
            "name": 'Ralph Test',
            "email": "test@test.com",
            "message": "Hello, This is a test",
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_contact_form_with_invalid_data(self):
        """
        Test the Contact form with invalid data
        """
        data = {}
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("email", form.errors)
        self.assertIn("message", form.errors)


class TestBookingForm(TestCase):
    """
    Test cases for the Booking form
    """
    def test_booking_form_is_valid(self):
        """
        Test the Booking form with valid data
        A portion of this test was writting by Jason Holt Smith
        """
        # Code below written by Jason Holt Smith
        user: User = User()
        user.save()
        chapel: Venue = Venue(
            venue_name="The Chapel",
            venue_capacity=5,
            staff_member=user
        )
        chapel.save()
        # End of JHS Code
        data = {
            "venue": chapel,
            "event_type": "Wedding",
            "event_date": "2024-09-18",
            "num_guests": 350,
            "client": 1,
        }
        form = BookingForm(data=data)
        self.assertTrue(form.is_valid(), json.dumps(form.errors))

    def test_booking_with_invalid_data(self):
        """
        Test the Booking form with invalid data
        """
        data = {}
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid(), json.dumps(form.errors))
