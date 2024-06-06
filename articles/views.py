from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import CommentForm



def get_posts():
    all_posts = Post.objects.all().order_by('date')
    return all_posts
'''
def get_comments():
    all_comments = Comment.objects.all().order_by('date')
    return all_comments
'''

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

#class PostView(DetailView):
 #   template_name = 'articles/post_page.html'
  #  model = Post

class PostView(View):
    def get(self, request, slug):
        single_post = get_object_or_404(Post, slug=slug)

        form = CommentForm()

        #all_comments = get_comments()

        return render(request, 'articles/post_page.html', {
            'post': single_post,
            'form': form,
            #'all_comments': all_comments
        })

    def post(self, request):
        single_post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            return HttpResponseRedirect('/thank-you')
        else:
            return render(request, 'articles/post_page.html', {
            'post': single_post,
            'form': form,
            #'all_comments': all_comments
        })

def thank_you(request):
    return render(request, 'articles/thank_you.html')