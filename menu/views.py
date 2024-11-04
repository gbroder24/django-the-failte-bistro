from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Dish
from .forms import CommentForm

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
    comments = dish.comments.all().order_by("-commented_on")
    comment_count = dish.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = dish
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "menu/menu_detail.html",
        {
            "dish": dish,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )