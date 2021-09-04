from django.shortcuts import render, redirect
from .models import Post
from .forms import Postform


def home(request):
    blogs = Post.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, 'front/home.html', context)

def post_list(request):
    posts = Post.objects.all()
    context = {
        'post_list' : posts
    }
    return render(request, 'back/post_list.html', context)

#CRUD starts here...
def post_detail(request, id):
    # In your detail template, you don't need a for loop; As you are just passing one post to the template:
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'front/post_detail.html', context)

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
    return render(request, 'back/create_post.html', context)

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
    return render(request, 'back/create_post.html', context)

def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    context = {
        'post' : post
    }
    return render(request, 'back/delete_post.html', context)