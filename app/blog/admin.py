from django.contrib import admin
from blog import models
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe
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
class PageAdmin(SummernoteModelAdmin):
    list_display = 'id', 'title', 'is_published', 'slug', 
    list_display_links = 'title',
    search_fields = 'id', 'title', 'slug',
    list_per_page = 10
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('title',),
    }
    summernote_fields = 'content',


@admin.register(models.Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = 'id', 'title', 'is_published',  'created_by',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'excerpt', 'content',
    list_per_page = 10
    list_filter = 'category', 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = 'created_at', 'updated_at', 'created_by', 'updated_by',\
                        'link',
    prepopulated_fields = {
        "slug": ('title',),
    }
    autocomplete_fields = 'tags', 'category',
    summernote_fields = ('content',)

    def link(self, obj):
        if not obj.pk:
            return '-'
        
        url_post = obj.get_absolute_url()
        safe_url = mark_safe(
            f'<a target="_blank" href="{url_post}">Ver Post</a>'
        )

        return safe_url

    # change: aponta se esse model está sendo alterado ou sendo criando
    # retornando um booleano
    def save_model(self, request, obj: models.Post, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user

        obj.save()
