from django.contrib import admin
from site_setup import models

# Register your models here.

@admin.register(models.MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path', 'new_tab',
    list_display_links = 'id', 'text', 'url_or_path', 'new_tab',
    search_fields = 'id', 'text', 'url_or_path', 'new_tab',


@admin.register(models.SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',

    def has_add_permission(self, request):
        return not models.SiteSetup.objects.all()[:1].exists()