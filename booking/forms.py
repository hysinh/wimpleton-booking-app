from .widgets import DatePickerInput
from django import forms
from django.core.validators import MaxValueValidator
from django.utils.timezone import now
from datetime import timedelta
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
        today = now()
        first_available_date = today + timedelta(days=5)
        two_years = today + timedelta(days=730)
        attrs.setdefault('min', first_available_date.strftime('%Y-%m-%d'))
        attrs.setdefault('max', two_years.strftime('%Y-%m-%d'))
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
            'event_date': DateInput()
        }

    
    # def clean_num_guests(self):
    #     data = self.cleaned_data['num_guests']
    #     if data > 500:
    #         raise ValidationError("Guest count exceeds maximum. Please adjust to 500 guests or less")
    # assign error message to num_guest field - not working
    # def clean(self):
    #     cleaned_data = super().clean()
    #     num_guests = cleaned_data.get("num_guests")

        # if num_guests > 500:
        #     msg = "Guest count exceeds maximum!"
        #     self.add_error("num_guests", msg)


    # def clean(self):
    #     if self.cleaned_data.get('num_guests') > 500:
    #         raise BookingForm.ValidationError('Guest count exceeds maximum!')
    #     return self.cleaned_data

    # def __init__(self, *args, **kwargs):
    #     super(BookingForm, self).__init__(*args, **kwargs)

    #     # adds custom error messages
    #     self.fields['num_guests'].error_messages.update({'Guest count cannot exceed 500 people nor be less than 20 people'})
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['num_guests'].validators.append(MaxValueValidator(500))

    


