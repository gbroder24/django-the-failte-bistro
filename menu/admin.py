from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Dish, Comment


@admin.register(Dish)
class MenuAdmin(SummernoteModelAdmin):

    list_display = ('dish_title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('dish_title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)