from django.shortcuts import render, redirect
from .models import Post
from .forms import Postform


def post_list(request):
    posts = Post.objects.all()
    context = {
        'post_list':posts
    }
    return render(request, 'post_list.html', context)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'post_detail.html', context)

def create_post(request):
    form = Postform()
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    context = {
        'form': form,
        'type': 'Create'
    }
    return render(request, 'create_post.html', context)

def update_post(request, id):
    post = Post.objects.get(id=id)
    form = Postform(instance=post)
    if request.method == 'POST':
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    context = {
        'form': form,
        'type': 'Update' 
    }
    return render(request, 'create_post.html', context)