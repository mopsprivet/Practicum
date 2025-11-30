from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import NewUserCreationForm
from django.contrib.auth import get_user_model
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm


User = get_user_model()

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("users:profile", username=request.user.username)
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, "auth/edit_profile.html", {"form": form})


def profile(request, username):
    user = User.objects.get(username=username)

    posts = Post.objects.filter(author=user).order_by('-pub_date')

    context = {
        "profile_user": user,
        "posts": posts,
    }
    return render(request, "auth/profile.html", context)



def register(request):
    if request.method == "POST":
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = NewUserCreationForm()

    return render(request, "auth/registration.html", {"form": form})
