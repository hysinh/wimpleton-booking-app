from django import forms
from .widgets import FengyuanChenDatePickerInput
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

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)


class DateForm(forms.Form):
    date = forms.DateField(input_formats=['%d/%m/%Y'])

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'], 
        widget=FengyuanChenDatePickerInput()
    )