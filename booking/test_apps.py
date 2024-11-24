from django.apps import apps
from django.test import TestCase
from booking.apps import BookingConfig


class TestBookingConfig(TestCase):
    """Tests the Django app config."""
    def test_app(self):
        self.assertEqual('booking', BookingConfig.name)
        self.assertEqual('booking', apps.get_app_config('booking').name)
