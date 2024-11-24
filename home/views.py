from django.shortcuts import render

# Create your views here.


def indexpage(request):
    """
    A view to return the index page
    """
    return render(request, 'home/index.html')
