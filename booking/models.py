from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import datetime

HOURS = (
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),
    ('22:30', '22:30'),
    ('23:00', '23:00'),
    ('23:30', '23:30'),
)

GUESTS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
)


def validate_date(date):
    if date < datetime.date.today():
        raise ValidationError(
            "Invalid date!",
            params={'date': date},
        )


# Create your models here.

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_reservation')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date = models.DateField(validators=[validate_date])
    time = models.CharField(choices=HOURS, default='19:00', max_length=13)
    num_of_guests = models.IntegerField(choices=GUESTS, default=4)
    phoneValidate = RegexValidator(
        regex = r'^[0-9]+$',
        message = "Enter a valid phone number.",
        code = "Invalid Number" 
        )
    contact_num = models.CharField(validators=[phoneValidate], max_length=13)


    class Meta:
        ordering = ['-time', '-date']
        unique_together = ['date', 'time']


    def __str__(self):
        return f"Reservation for {self.first_name} {self.last_name} on the {self.date} at {self.time}"