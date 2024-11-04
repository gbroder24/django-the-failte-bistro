from . import views
from django.urls import path

urlpatterns = [
    path('reservations/', views.reservations, name='reservations'),
    path('new_booking/', views.create_booking, name='create_booking'),
]