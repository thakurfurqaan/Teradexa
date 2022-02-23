from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm, CreatePostForm
from .models import Post


# User Authentication

@login_required
def dashboard(request):
    posts = Post.objects.filter(user=request.user)
    context = {
        'posts': posts,
    }
    return render(request, 'authapp/dashboard.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'authapp/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'authapp/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'authapp/edit.html', context=context)


# Posting Feature

@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = CreatePostForm(request.POST)
        post_form.instance.user = request.user
        if post_form.is_valid():
            post_form.save()
            print("Post saved successfully")
        else: 
            print("Post NOT saved successfully")
    else:
        post_form = CreatePostForm(instance=request.user)
    context = {
        'form': post_form,
    }
    return render(request, 'post/create_post.html', context=context)
