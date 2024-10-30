"""
URL configuration for failte_bistro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from home import views as index_views
# from about import views as about_views
# from menu import views as menu_views
# from booking import views as booking_views

urlpatterns = [
    path('about/', include('about.urls'), name='about-urls'),
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls'), name='booking-urls'),
    path('', include('home.urls'), name='home-urls'),
    path('summernote/', include('django_summernote.urls')),
    path('menu/', include('menu.urls'), name='menu-urls'),
    # path('menu/', menu_views.menu_failte_bistro, name='menu'),
    
]
