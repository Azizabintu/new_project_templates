from django.contrib import admin
from .models import Category, News
# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published_time', 'status']
    list_filter = ['status', 'published_time', 'created_time']
    prepopulated_fields = {"slug": ('title',)}
    date_hierarchy = 'published_time'
    search_fields = ['status', 'body']
    ordering = ['status','published_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
