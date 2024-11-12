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
    Display an individual dish.

    **Context**
    ``dish``: The dish object being viewed.
    ``comments``: A list of comments on the dish.
    ``comment_count``: Total number of approved comments.
    ``heart_count``: Total number of hearts (likes) given to the dish.
    ``comment_form``: Form to submit a comment.

    **Template**: menu/menu_detail.html
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

    if request.method == "POST" and "heart" in request.POST:
        if request.user.is_authenticated:
            # Check if the user already "hearts" the dish
            if dish.hearts.filter(id=request.user.id).exists():
                # Remove heart
                dish.hearts.remove(request.user)
                messages.add_message(
                    request, messages.INFO,
                    'You unhearted this dish.'
                )
            else:
                # Add heart
                dish.hearts.add(request.user)
                messages.add_message(
                    request, messages.SUCCESS,
                    'You hearted this dish!'
                )
        else:
            messages.add_message(
                request, messages.WARNING,
                'You need to be logged in to heart a dish.'
            )
    
    heart_count = dish.hearts.count()
    comment_form = CommentForm()
    

    return render(
        request,
        "menu/menu_detail.html",
        {
            "dish": dish,
            "comments": comments,
            "comment_count": comment_count,
            "heart_count": heart_count,
            "comment_form": comment_form,
        },
    )