from django.test import TestCase
from .forms import BookingForm, EmailForm

# Create your tests here.
class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        booking_form = BookingForm(
            {'venue': '1'},
            {'event_type': 'Wedding'},
            {'event_date': '2024-10-20'},
            {'num_guests': '250'}
        )
        self.assertTrue(booking_form.is_valid())
