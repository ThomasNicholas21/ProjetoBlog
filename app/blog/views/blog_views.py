from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from blog.models import Post, Page
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404
from django.views.generic.list import ListView

PER_PAGE = 6

# def index(request):
#     posts = Post.objects.get_published()

#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return render(
#         request,
#         'blog/pages/index.html',
#         {
#             'page_obj': page_obj,
#             'page_title': 'Home -',
#         }
#     )


class PostListView(ListView):
    model = Post
    template_name = 'blog/pages/index.html'
    context_object_name = 'posts'
    ordering = '-pk'
    paginate_by = PER_PAGE
    queryset = Post.objects.get_published()
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_published=True)
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            {'page_title': 'Home -'}
        )

        return context


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
    
    page_title = f'{search_values[:15]} - Search - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': posts,
            'page_title': page_title,
        }
    )


def created_by(request, author_id):
    user = User.objects.filter(pk=author_id).first()
    user_full_name = user.username

    if user is None:
        raise Http404('User not found')
    
    if user.first_name:
        user_full_name = f'{user.first_name} {user.last_name}'

    page_title = 'Posts de' + user_full_name
    
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
            'page_title': page_title,
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

    if len(posts) == 0:
        raise Http404()

    page_title = f'{page_obj[0].category.name} - Categoria - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
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

    if len(posts) == 0:
        raise Http404()
    
    page_title = f'{page_obj[0].tags.first().name} - Tags - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
        }
    )


def page_view(request, slug):
    page = Page.objects.filter(is_published=True).filter(slug=slug).first()

    if page is None:
        raise Http404()

    page_title = f'{page} - Page - '

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page,
            'page_title': page_title,
        }
    )


def post_view(request,slug):
    post = Post.objects.get_post(slug)

    if post is None:
        raise Http404()

    page_title = f'{post} - Post -'

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post,
            'page_title': page_title,
        }
    )
