from django.shortcuts import render
from django.views import generic
from .models import Menu

# Create your views here.
class MenuList(generic.ListView):
    queryset = Menu.objects.filter(status=1)
    template_name = "menu_list.html"