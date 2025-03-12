"""
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('page/<slug:slug>/', views.page, name='page'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('created_by/<int:author_id>/', views.created_by, name='created_by'),
    path('created_by/<str:slug>/', views.category_view, name='category'),
    path('tag/<str:slug>/', views.tag_view, name='tag'),
    path('tag/<str:slug>/', views.tag_view, name='tag'),

]
