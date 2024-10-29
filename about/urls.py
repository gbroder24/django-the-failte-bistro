from . import views
from django.urls import path

urlpatterns = [
    path('about/', views.aboutpage, name='about'),
]