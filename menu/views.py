from django.shortcuts import render
from django.views import generic
from .models import Menu

# Create your views here.
class MenuList(generic.ListView):
    model = Menu