from .widgets import DatePickerInput
from django import forms
from .models import Booking, Venue

TYPE_OF_EVENT_CHOICES = {
        ("WED", "Wedding"),
        ("COR", "Corporate Event"),
        ("GAL", "Gala Event"),
        ("OCC", "Special Occasion"),
        ("WSP", "Workshop"),
        ("OTH", "Other"),
    }

VENUES = {
        ("The Chapel"),
        ("The Mansion Formal Rooms"),
        ("The Conservatory"),
        ("OCC"),
    }


     
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'venue',
            'event_type',
            'event_date',
            'num_guests'
        ]

        widgets = {
            'event_date': DatePickerInput()
        }


