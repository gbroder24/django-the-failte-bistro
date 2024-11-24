from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .forms import CommentForm
from .models import Dish, Comment

# Create your views here.
class MenuList(generic.ListView):
    queryset = Dish.objects.filter(status=1)
    template_name = "menu/menu_list.html"


def menu_detail(request, slug):
    """
    Renders the most recent dish a user selects.
    Displays instance of :model:`auth.User`.
    Displays instance of :model:`menu.Dish`.

    **Context**
    ``dish``: The dish object being viewed.
    ``comments``: A list of comments on the dish.
    ``comment_count``: Total number of approved comments.
    ``like_count``: Total number of likes (likes) given to the dish.
    ``heart_count``: Total number of hearts (love) given to the dish.
    ``comment_form``: Form to submit a comment.

    **Template:**
    :template: `menu/menu_detail.html`
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
                    'You did not love this dish.'
                )
            else:
                # Add heart
                dish.hearts.add(request.user)
                messages.add_message(
                    request, messages.SUCCESS,
                    'You loved this dish!'
                )
        else:
            messages.add_message(
                request, messages.WARNING,
                'You need to be logged in to heart a dish.'
            )

    # Handle liking a comment
    if request.method == "POST" and "like" in request.POST:
        comment_id = request.POST.get("comment_id")
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user.is_authenticated:
            # Check if the user already liked the comment
            if request.user in comment.likes.all():
                comment.likes.remove(request.user)
                messages.add_message(
                    request, messages.INFO,
                    'You unliked this comment.'
                )
            else:
                comment.likes.add(request.user)
                messages.add_message(
                    request, messages.SUCCESS,
                    'You liked this comment!'
                )
        else:
            messages.add_message(
                request, messages.WARNING,
                'You need to be logged in to like a comment.'
            )

    # Calculate comment counts
    comment_count = dish.comments.count()

    # Calculate heart counts
    heart_count = dish.hearts.count()

    # Include the like count for each comment
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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments

    **Context**
    ``dish``: The dish object being viewed.
    ``comments``: A list of comments on the dish.
    ``like_count``: Total number of likes (likes) given to the dish.
    ``comment_form``: Form to submit a comment.
    """

    if request.method == "POST":

        queryset = Dish.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('menu_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment

     **Context**
    ``dish``: The dish object being viewed.
    ``comments``: A list of comments on the dish.
    ``like_count``: Total number of likes (likes) given to the dish.
    ``comment_form``: Form to submit a comment.
    """
    queryset = Dish.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('menu_detail', args=[slug]))
