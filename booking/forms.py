from django import forms
import datetime
from .models import Reservation


class DateInput(forms.DateInput):
    """
    Provides the user with a UI Calendar to select date
    entry.
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    Form class for users to request a booking
    """
    class Meta:
        model = Reservation
        fields = (
            'first_name',
            'last_name',
            'date',
            'time',
            'num_of_guests',
            'contact_num',
        )
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date': 'Date',
            'time': 'Time',
            'num_of_guests': 'Number Of Guests',
            'contact_num': 'Contact Number',
        }
        widgets = {
            'date': DateInput()
        }
