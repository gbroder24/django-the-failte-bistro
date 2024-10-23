from django.shortcuts import render
from django.views import generic
from .models import Dish

# Create your views here.
class MenuList(generic.ListView):
    queryset = Dish.objects.filter(status=1)
    template_name = "menu/menu_list.html"
    paginate_by = 6