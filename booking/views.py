from django.shortcuts import render

# Create your views here.
def bookingpage(request):
    return render(request, 'booking/booking.html')