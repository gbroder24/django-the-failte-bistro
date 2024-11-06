from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reservation
from .forms import BookingForm

# Create your views here.


def reservations(request):
    """
    The View that renders the reservations.html
    which shows all bookings made by the current user
    or gives link to make a booking if no reservations made
    or redirects to signup page if user is not signed in.
    """
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(
            customer=request.user.id).order_by('-date')
        context = {
            'reservations': reservations
        }
        return render(request, 'booking/reservations.html', context)
    else:
        return redirect('/accounts/login')


def create_booking(request):
    """
    Renders the Create Booking Page, presents the user
    with a form and validation to submit details for
    desired booking for the guest.
    """
    if request.method == 'POST':
        print("Received a POST request")
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            reservation = booking_form.save(commit=False)
            reservation.customer = request.user
            reservation.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Reservation Confirmed, We Look Forward to Seeing you")
            return redirect('reservations')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                list(booking_form.errors.values())[0])
    booking_form = BookingForm()
    print("About to render template")
    return render(
        request,
        "booking/create_booking.html",
        {'booking_form': booking_form}
    )