"""
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<slug:slug>/', views.page, name='page'),
    path('post/<slug:slug>/', views.post, name='post'),
]
