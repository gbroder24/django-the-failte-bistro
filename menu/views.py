from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Dish

# Create your views here.
class MenuList(generic.ListView):
    queryset = Dish.objects.filter(status=1)
    template_name = "menu/menu_list.html"


def menu_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Dish.objects.filter(status=1)
    dish = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "menu/menu_detail.html",
        {"dish": dish},
    )