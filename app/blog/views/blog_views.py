from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from blog.models import Post, Page
from django.db.models import Q

PER_PAGE = 9

def index(request):
    posts = Post.objects.get_published()

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def search(request):
    search_values = request.GET.get('q', '').strip()

    if search_values == '':
        return redirect('blog:index')
    
    posts = (
        Post.objects.get_published()
        .filter(
            Q(title__icontains=search_values) |
            Q(excerpt__icontains=search_values) 
        ).order_by('-id')[:PER_PAGE]
    )

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': posts,
        }
    )


def created_by(request, author_id):
    posts = (
        Post.objects.get_published()
        .filter(created_by__pk=author_id)
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def category_view(request, slug):
    posts = (
        Post.objects.get_published()
        .filter(category__slug=slug)
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def tag_view(request, slug):
    posts = (
        Post.objects.get_published()
        .filter(tags__slug=slug)
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def page(request, slug):
    page = Page.objects.filter(is_published=True).filter(slug=slug).first()

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page,
        }
    )


def post(request,slug):
    post = Post.objects.get_post(slug)


    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post,
        }
    )
