from .widgets import DatePickerInput
from django import forms
from django.utils.timezone import now
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Booking

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

# DateInput Source: 
# https://stackoverflow.com/questions/74227268/how-to-make-a-date-picker-that-does-not-select-previous-dates-in-django
class DateInput(forms.DateInput):
    input_type = 'date'

    def get_context(self, name, value, attrs):
        attrs.setdefault('min', now().strftime('%Y-%m-%d'))
        return super().get_context(name, value, attrs)
     
     
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
            # 'event_date': DatePickerInput(),
            'event_date': DateInput()
        }


    


