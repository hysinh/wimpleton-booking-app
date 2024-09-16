from .widgets import DatePickerInput
from django import forms
from django.core.validators import MaxValueValidator
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
            'event_date': DateInput()
        }

    
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

    


