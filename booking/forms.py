from django import forms
from django.utils.timezone import now
from datetime import timedelta
from .models import Booking, Contact


# DateInput Source:
# https://stackoverflow.com/questions/74227268/how-to-make-a-date-picker-that-does-not-select-previous-dates-in-django
# Assistance in figuring out how to use timedelta and setting a max
# time limit by CI Mentor, Sandeep Aggarwal
class DateInput(forms.DateInput):
    """
    Creates a Date picker for the Booking form.
    Sets available dates for a minimum of 5 days from today's
    date and a maximum of two years from today's date.
    """
    input_type = "date"

    def get_context(self, name, value, attrs):
        today = now()
        first_available_date = today + timedelta(days=5)
        two_years = today + timedelta(days=730)
        attrs.setdefault("min", first_available_date.strftime("%Y-%m-%d"))
        attrs.setdefault("max", two_years.strftime("%Y-%m-%d"))
        return super().get_context(name, value, attrs)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["venue", "event_type", "event_date", "num_guests"]

        widgets = {"event_date": DateInput()}


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
