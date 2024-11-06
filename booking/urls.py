from . import views
from django.urls import path

urlpatterns = [
    path('new_booking/', views.create_booking, name='create_booking'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/delete/<reservation_id>', views.delete_reservation, name='edit'),
    path('reservations/edit/<reservation_id>', views.edit_reservation, name='edit'),
]