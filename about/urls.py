from . import views
from django.urls import path

urlpatterns = [
    path('', views.aboutpage, name='about'),
]