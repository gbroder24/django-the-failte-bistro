from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuList.as_view(), name='menu'),
    path('dish/<slug:slug>/', views.menu_detail, name='menu_detail'),
    path('<slug:slug>/', views.menu_detail, name='menu_detail'),
]