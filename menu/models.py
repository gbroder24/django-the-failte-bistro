from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Dish(models.Model):
    """
    Stores a single dish entry related to :model:`auth.User`.
    """

    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
    ]

    dish_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dish_posts")
    content = models.TextField()
    posted_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    hearts = models.ManyToManyField(User, blank=True, related_name="hearts")
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    featured_image = CloudinaryField('image', default='placeholder')
    

    class Meta():
        ordering = ["-posted_on"]


    def __str__(self):
        return f"{self.dish_title}"


    def save(self, *args, **kwargs):
        """
        Method to enforce image upload restriction to admins only.
        Check if image is being added by a non-admin user.
        """
        if self.featured_image != 'placeholder' and not self.author.is_staff:
            raise ValidationError("Only admin can upload images.")

        super(Dish, self).save(*args, **kwargs)


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`menu.Dish`.
    """
    post = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    commented_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")

    class Meta():
        ordering = ["commented_on"]


    def __str__(self):
        return f"Comment: {self.content} by {self.author} "