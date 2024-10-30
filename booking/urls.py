from . import views
from django.urls import path

urlpatterns = [
    path('', views.bookingpage, name='booking'),
]