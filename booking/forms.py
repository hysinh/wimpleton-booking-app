from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    """
    Creates the booking form with the field of 'venue',
    'event_type', 'event_date', and 'num_guests' as related to :model:'auth.User'.
    """
    class Meta:
        model = Booking
        fields = [
            'venue',
            'event_type',
            'event_date',
            'num_guests'
        ]