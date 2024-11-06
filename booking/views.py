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


def edit_reservation(request, reservation_id):
    """
    The view for editing a currently existing booking, validates the current user
    or redirects back to reservations. Autofills form with current data stored
    in the booking.
    """
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.user == reservation.customer:
        if request.method == 'POST':
            booking_form = BookingForm(data=request.POST, instance=reservation)
            if booking_form.is_valid():
                reservation.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Booking Updated. See you soon!")
                return redirect('reservations')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    list(booking_form.errors.values())[0])
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "ERROR: Only the Guest who made the reservation has permission to change a reservation."
        )
        return redirect('reservations')
    booking_form = BookingForm(instance=reservation)
    return render(
        request,
        "booking/edit_booking.html",
        {'booking_form': booking_form}
    )


def delete_reservation(request, reservation_id):
    """
    The View that deletes the desired booking, requires the
    user that made the booking otherwise will redirect back
    to reservations.
    """
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.user == reservation.customer:
        reservation.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Your reservation has been cancelled."
        )
        return redirect('reservations')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "ERROR: Only the Guest who made the reservation has permission to cancel."
        )
        return redirect('reservations')