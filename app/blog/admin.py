from django.contrib import admin
from blog import models
# Register your models here.
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug', 
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug', 
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'slug', 
    list_display_links = 'title',
    search_fields = 'id', 'title', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('title',),
    }


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    # list_display = 'id', 'title', 'is_published', 'created_by', 
    # list_display_links = 'title',
    # search_fields = 'id', 'title', 'slug', 'title', 'excerpt', 'content', 'cover',
    # list_per_page = 10
    # list_filter = 'category', 'is_published',
    # list_editable = 'is_published', 
    # ordering = '-id',
    # readonly_fields = 'created_at', 'update_at', 'update_by', 'created_by', 'updated_by', 
    # prepopulated_fields = {
    #     'slug': ('title',),
    # }
    # autocomplete_fields = 'tags', 'category',
    ...
