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