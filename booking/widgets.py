from django import forms

# Source: https://forum.djangoproject.com/t/need-help-with-date-time-picker/16988
class DatePickerInput(forms.DateInput):
    input_type = 'date'