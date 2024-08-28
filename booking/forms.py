from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Creates the booking form as related to :model:'auth.User'.
    """
    class Meta:
        model = Booking
        fields = [
            'venue',
            'event_type',
            'event_date',
            'num_guests'
        ]