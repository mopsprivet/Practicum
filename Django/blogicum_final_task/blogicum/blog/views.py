from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.functions import Now
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils import timezone

from .models import Post, Category, Comment
from blogicum.constants import RECENT_POSTS_COUNT, POSTS_PER_PAGE
from .forms import PostForm, CommentForm, RegistrationForm, ProfileForm

def published_posts(manager):
    return manager.select_related('category', 'location', 'author').filter(
        pub_date__lte=Now(),
        is_published=True,
        category__is_published=True
    )

def paginate_queryset(request, queryset, POSTS_PER_PAGE):
    paginator = Paginator(queryset, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def index(request):
    template = 'blog/index.html'
    posts = published_posts(Post.objects).order_by('-pub_date')
    page_obj = paginate_queryset(request, posts, POSTS_PER_PAGE)
    context = {'page_obj': page_obj}
    return render(request, template, context)

def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        pk=post_id
    )

    if not (post.pub_date <= timezone.now() or request.user == post.author):
        return render(request, 'pages/404.html', status=404)
    if not post.is_published and request.user != post.author:
        return render(request, 'pages/404.html', status=404)
    if not post.category.is_published and request.user != post.author:
        return render(request, 'pages/404.html', status=404)

    comment_form = CommentForm()
    context = {
        'post': post,
        'form': comment_form,
        'comments': post.comments.all()
    }
    return render(request, template, context)

def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    posts = published_posts(category.posts).order_by('-pub_date')
    page_obj = paginate_queryset(request, posts, POSTS_PER_PAGE)
    context = {'category': category, 'page_obj': page_obj}
    return render(request, template, context)

@login_required
def create_post(request):
    template = 'blog/create.html'
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('blog:profile', username=request.user.username)
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, template, context)

@login_required
def edit_post(request, post_id):
    template = 'blog/create.html'
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        return redirect('blog:post_detail', post_id=post.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    
    context = {'form': form}
    return render(request, template, context)

@login_required
def delete_post(request, post_id):
    template = 'blog/create.html'
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        return redirect('blog:post_detail', post_id=post.pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:profile', username=request.user.username)
    
    context = {'form': PostForm(instance=post)}
    return render(request, template, context)

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', post_id=post.pk)
    return redirect('blog:post_detail', post_id=post.pk)

@login_required
def edit_comment(request, post_id, comment_id):
    template = 'blog/comment.html'
    comment = get_object_or_404(Comment, pk=comment_id, post_id=post_id)
    if request.user != comment.author:
        return redirect('blog:post_detail', post_id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', post_id=post_id)
    else:
        form = CommentForm(instance=comment)
    
    context = {'form': form, 'comment': comment}
    return render(request, template, context)

@login_required
def delete_comment(request, post_id, comment_id):
    template = 'blog/comment.html'
    comment = get_object_or_404(Comment, pk=comment_id, post_id=post_id)
    if request.user != comment.author:
        return redirect('blog:post_detail', post_id=post_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('blog:post_detail', post_id=post_id)
    
    context = {'comment': comment}
    return render(request, template, context)

def registration_view(request):
    template = 'registration/registration_form.html'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:profile', username=user.username)
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, template, context)

@login_required
def profile(request, username):
    template = 'blog/profile.html'
    user = get_object_or_404(User, username=username)
    # автор видит все свои посты, другие видят только опубликованные и непоздние
    if request.user == user:
        qs = user.post_set.all().select_related('category', 'location')
    else:
        qs = published_posts(user.post_set).order_by('-pub_date')
    page_obj = paginate_queryset(request, qs, POSTS_PER_PAGE)
    context = {
        'profile': user,
        'page_obj': page_obj
        }
    return render(request, template, context)

@login_required
def edit_profile(request):
    template = 'blog/user.html'
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile', username=request.user.username)
    else:
        form = ProfileForm(instance=request.user)
    
    context = {'form': form}
    return render(request, template, context)
