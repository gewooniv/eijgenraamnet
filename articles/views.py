from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'articles/index.html')

def posts(request):
    return render(request, 'articles/posts.html')

def post_page(request, slug):
    return render(request, 'articles/post_page.html')