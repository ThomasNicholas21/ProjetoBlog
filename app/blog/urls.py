"""
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('search/', views.SearchViewList.as_view(), name='search'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('post/<slug:slug>/', views.post_view, name='post'),
    path('created_by/<int:author_id>/', views.CreatedByListView.as_view(), name='created_by'),
    path('category/<str:slug>/', views.CategoryListView.as_view(), name='category'),
    path('tag/<str:slug>/', views.TagListView.as_view(), name='tag'),
]
