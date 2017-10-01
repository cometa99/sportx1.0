from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def post_create(request):
    context = {
       "title": "create post new"

       }
    return render(request, "index.html", context)

def post_detail(request):
    instance = get_object_or_404(Post, id=22)
    context = {
       "title": instance.title,
       "instance": instance,

       }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
       "object_list": queryset,
       "title": "Loteria Nacional"

    }
    return render(request, "index.html", context)

def post_update(request):
    context = {
       "title": "update post"
       }
    return render(request, "index.html", context)

def post_delete(request):
    context = {
       "title": "delete post"
       }
    return render(request, "index.html", context)

def post_quiniela_pale(request):
    queryset = Post.objects.all()
    context = {
       "object_list": queryset,
       "title": "Quiniela Pale"

    }
    return render(request, "index.html", context)
