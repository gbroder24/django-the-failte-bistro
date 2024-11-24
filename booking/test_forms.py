from django.test import TestCase
from .forms import BookingForm

# Create your tests here.


class TestBookingForm(TestCase):
    """
    Test suite for testing the booking form validation
    """

    def test_booking_is_valid(self):
        """
        Test valdation for all fields
        """
        booking_form = BookingForm({
            'first_name': 'John',
            'last_name': 'Jones',
            'date': '2024-11-20',
            'time': '18:00',
            'num_of_guests': '2',
            'contact_num': '0812345678',
            })
        self.assertTrue(booking_form.is_valid(), msg='Form is not valid')

    def test_booking_first_name_invalid(self):
        """
        Test validation for the empty First name field
        """
        booking_form = BookingForm({
            'first_name': '',
            'last_name': 'Jones',
            'date': '2024-11-20',
            'time': '18:00',
            'num_of_guests': '2',
            'contact_num': '0812345678',
            })
        self.assertFalse(booking_form.is_valid(),
                         msg='First name was not provided,'
                         'but the form is valid')

    def test_booking_last_name_invalid(self):
        """
        Test validation for the empty Last name field
        """
        booking_form = BookingForm({
            'first_name': 'John',
            'last_name': '',
            'date': '2024-11-20',
            'time': '18:00',
            'num_of_guests': '2',
            'contact_num': '0812345678',
            })
        self.assertFalse(booking_form.is_valid(),
                         msg='Last name was not provided,'
                         'but the form is valid')

    def test_booking_date_invalid(self):
        """
        Test validation for the empty date field
        """
        booking_form = BookingForm({
            'first_name': 'John',
            'last_name': 'Jones',
            'date': '',
            'time': '18:00',
            'num_of_guests': '2',
            'contact_num': '0812345678',
            })
        self.assertFalse(booking_form.is_valid(),
                         msg='Date was not provided, but the form is valid')

    def test_booking_time_invalid(self):
        """
        Test validation for the empty time field
        """
        booking_form = BookingForm({
            'first_name': 'John',
            'last_name': 'Jones',
            'date': '2024-11-20',
            'time': '',
            'num_of_guests': '2',
            'contact_num': '0812345678',
            })
        self.assertFalse(booking_form.is_valid(),
                         msg='Time was not provided, but the form is valid')

    def test_booking_num_of_guests_invalid(self):
        """
        Test validation for the empty number of guests field
        """
        booking_form = BookingForm({
            'first_name': 'John',
            'last_name': 'Jones',
            'date': '2024-11-20',
            'time': '18:00',
            'num_of_guests': '',
            'contact_num': '0812345678',
            })
        self.assertFalse(booking_form.is_valid(),
                         msg='Number of guests was not provided,'
                         'but the form is valid')

    def test_booking_contact_num_invalid(self):
        """
        Test validation for the empty contact number time field
        """
        booking_form = BookingForm({
            'first_name': 'John',
            'last_name': 'Jones',
            'date': '2024-11-20',
            'time': '18:00',
            'num_of_guests': '2',
            'contact_num': '',
            })
        self.assertFalse(booking_form.is_valid(),
                         msg='Contact number was not provided,'
                         'but the form is valid')
