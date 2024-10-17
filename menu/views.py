from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu_failte_bistro(request):
    return HttpResponse("This must be the menu page.")
