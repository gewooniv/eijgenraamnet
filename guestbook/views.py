from datetime import date

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Comment
from .forms import CommentForm

# Create your views here.

def get_comments():
    all_comments = Comment.objects.filter(comment__isnull=True).order_by('date')
    return all_comments

def get_responses():
    all_responses = Comment.objects.filter(comment__isnull=False).order_by('date')
    return all_responses

class GuestbookView(View):
    def get(self, request):
        context = {
            'comment_form': CommentForm(),
            'all_comments': get_comments(),
            'all_responses': get_responses()
        }
        return render(request, 'guestbook/guestbook.html', context)
    
    def post(self, request):
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.date = date.today()
            comment.save()

            context = {
                'comment_form': form,
                'all_comments': get_comments(),
                'all_responses': get_responses()
            }

            return HttpResponseRedirect(reverse('guestbook'))
        else:
            context = {
            'comment_form': CommentForm(),
            'all_comments': get_comments(),
            'all_responses': get_responses()
            }

            return render(request, 'guestbook/guestbook.html', context)

def add_response(request):
    add_comment_form = ""
    return render_to_string('guestbook', {'add_comment_form': add_comment_form}, request)