"""
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    # permite que o dev tenha acesso aos arquivos enviados pelo user
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # permite que o dev tenha acesso aos arquivos estáticos
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
