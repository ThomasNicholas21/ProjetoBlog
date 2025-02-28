"""
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.urls import path
from blog import views

app_name = 'site_setup'

urlpatterns = [
    path('', views.index, name='index'),
]
