from . import views
from django.urls import path

urlpatterns = [
    path('menu/', views.MenuList.as_view(), name='menu'),
]