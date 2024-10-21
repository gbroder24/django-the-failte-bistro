from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Menu(models.Model):
    dish_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dish_posts")
    content = models.TextField()
    posted_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    hearts = models.ManyToManyField(User, blank=True, related_name="hearts")
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(default=timezone.now)


    class Meta():
        ordering = ["-posted_on"]


    def __str__(self):
        return f"{self.dish_title}"


class Comment(models.Model):
    post = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    commented_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")

    class Meta():
        ordering = ["commented_on"]


    def __str__(self):
        return f"Comment: {self.content} by {self.author} "