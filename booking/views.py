from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BookingForm
from .models import Reservation

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
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.guest = request.user
            booking.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Booking Confirmed, We Look Forward to Seeing you")
            return redirect('reservations')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                list(form.errors.values())[0])
    form = BookingForm()
    return render(
        request,
        "booking/create_booking.html",
        {'booking_form': form}
    )