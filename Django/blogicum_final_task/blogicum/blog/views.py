from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Now

from .models import Post, Category


def published_posts(manager):
    return manager.select_related('category', 'location').filter(
        pub_date__lte=Now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    template = 'blog/index.html'
    posts = published_posts(Post.objects)[:5]
    context = {
        'post_list': posts
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        published_posts(Post.objects),
        pk=post_id
    )
    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = published_posts(Post.objects).filter(category=category)
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, template, context)
