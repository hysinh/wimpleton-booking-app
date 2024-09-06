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


class RequestBookingForm(forms.Form):
    venue = forms.ModelMultipleChoiceField(
        queryset=Venue.objects.filter(status=1),
        widget=forms.Select(),
        )
    event_date = forms.DateField(required=True)
    event_type = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.Select(choices=TYPE_OF_EVENT_CHOICES),
        )
    num_guests = forms.IntegerField(required=True)



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

    # def __init__(self, *args, **kwargs):
    #     super(BookingForm, self).__init__(*args, **kwargs)


# class DateForm(forms.Form):
#     date = forms.DateField(input_formats=['%d/%m/%Y'])

# class DateForm(forms.Form):
#     date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'], 
#         widget=FengyuanChenDatePickerInput()
#     )