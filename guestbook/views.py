from datetime import date

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import render

from .models import Comment
from .forms import CommentForm

# Create your views here.

def get_comments():
    all_comments = Comment.objects.order_by('date')
    return all_comments

class GuestbookView(View):
    def get(self, request):
        context = {
            'comment_form': CommentForm(),
            'all_comments': get_comments()
        }
        return render(request, 'guestbook/guestbook.html', context)
    
    def post(self, request):
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.date = date.today()
            context = {
                'comment_form': form,
                'all_comments': get_comments()
            }

            return HttpResponseRedirect(reverse('guestbook'))
        else:
            context = {
            'comment_form': CommentForm(),
            'all_comments': get_comments()
            }

            return render(request, 'guestbook/guestbook.html', context)
