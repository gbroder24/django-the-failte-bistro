from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Reservation
from .forms import BookingForm


class TestBookingView(TestCase):

    def setUp(self):
        """
        Set up user and reservation data
        """
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

        self.reservation = Reservation(
            customer=self.user,
            first_name= 'John',
            last_name= 'Jones',
            date= '2024-11-20',
            time= '18:00',
            num_of_guests= '2',
            contact_num= '0812345678')

        self.reservation.save()

    def test_render_reservation_page(self):
        """
        Verifies get request for reservations page
        """
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.get(reverse('reservations'))
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John', response.content)
        self.assertIn(b'Jones', response.content)
        self.assertIn(b'Nov. 20, 2024', response.content)
        self.assertIn(b'18:00', response.content)
        self.assertIn(b'2', response.content)
        self.assertIn(b'0812345678', response.content)


    def test_render_create_booking_page(self):
        """
        Verifies get request for create booking page
        """
        response = self.client.get(reverse('create_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context['booking_form'], BookingForm)


    def test_successful_reservation_submission(self):
        """
        Test for posting a reservation
        """
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'first_name': 'John',
            'last_name': 'Jones',
            'date': '2024-11-20',
            'time': '18:00',
            'num_of_guests': '',
            'contact_num': '0812345678',
        }
        response = self.client.post(reverse(
            'reservations'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Your Reservations',
            response.content
        )
        