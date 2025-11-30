from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

from blogicum.constants import POSTS_PER_PAGE
from .forms import NewUserCreationForm
from blog.models import Post


User = get_user_model()

@login_required
def edit_profile(request):
    template = 'auth/edit_profile.html'
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=request.user.username)
    else:
        form = UserChangeForm(instance=request.user)
    
    context = {'form': form}

    return render(request, template, context)


def profile(request, username):
    template = 'auth/profile.html'
    user = User.objects.get(username=username)

    post_list = Post.objects.filter(
        author=user
    ).order_by('-pub_date')

    paginator = Paginator(post_list, POST_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'profile_user': user,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def register(request):
    template = 'auth/registration.html'
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = NewUserCreationForm()
    context = {'form': form}

    return render(request, template, context)
