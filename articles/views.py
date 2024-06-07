from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .models import Post, Comment
from .forms import CommentForm



def get_posts():
    all_posts = Post.objects.all().order_by('date')
    return all_posts

def get_comments():
    all_comments = Comment.objects.all().order_by('date')
    return all_comments

# Create your views here.
class MainPageView(ListView):
    template_name = 'articles/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'latest_posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class PostsView(ListView):
    template_name = 'articles/posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

class PostView(View):
    def get(self, request, slug):
        single_post = get_object_or_404(Post, slug=slug)

        context = {
            'post': single_post,
            'comment_form': CommentForm(),
            'all_comments': get_comments()
        }

        return render(request, 'articles/post-page.html', context)

    def post(self, request, slug):
        single_post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            
            comment = form.save(commit=False)
            comment.post = single_post
            comment.date = date.today()
            comment.save()

            return HttpResponseRedirect(reverse('post-page', args=[slug]))
        else:
            context = {
            'post': single_post,
            'comment_form': form,
            'all_comments': get_comments()
            }

            return render(request, 'articles/post-page.html', context)
