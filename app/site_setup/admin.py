from django.contrib import admin
from site_setup import models

# Register your models here.

@admin.register(models.MenuLink)
class MenuLink(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path', 'new_tab'
    list_display_links = 'id', 'text', 'url_or_path', 'new_tab'
    search_fields = 'id', 'text', 'url_or_path', 'new_tab'
