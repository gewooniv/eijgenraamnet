from datetime import date
from django.shortcuts import get_object_or_404, render

from .models import Post

def get_posts():
    all_posts = Post.objects.all().order_by('date')
    return all_posts

# Create your views here.

def main_page(request):
    posts = get_posts()
    latest_posts = posts[:3][::-1]
    return render(request, 'articles/index.html', {
        'latest_posts': latest_posts,
    })

def posts(request):
    posts = get_posts()
    return render(request, 'articles/posts.html', {
        'posts': posts,
    })

def post_page(request, slug):
    single_post = get_object_or_404(Post, slug=slug)
    return render(request, 'articles/post_page.html', {
        'post': single_post,
    })