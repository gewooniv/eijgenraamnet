from datetime import date

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import render

from .models import Comment
from .forms import CommentForm

# Create your views here.

def get_comments():
    all_comments = Comment.objects.filter(comment__isnull=True).order_by("-date")
    return all_comments

def get_responses():
    all_responses = Comment.objects.filter(comment__isnull=False).order_by("-date")
    return all_responses

def get_admins():
    all_admins = User.objects.filter(Q(is_staff=True) | Q(is_superuser=True))
    return all_admins

class GuestbookView(View):
    global context
    context = {
        "all_comments": get_comments(),
        "all_responses": get_responses(),
        "all_admins": get_admins(),
    }

    def get(self, request):
        context.update({'comment_form':CommentForm()})
        
        return render(request, "guestbook/guestbook.html", context)

    def post(self, request):
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment_id = request.POST["comment_id"]
            if comment_id:
                comment.comment = Comment.objects.get(pk=comment_id)
            comment.date = date.today()
            comment.save()

            context.update({"comment_form": form})

            return HttpResponseRedirect(reverse("guestbook"))
        else:
            context.update({'comment_form':CommentForm()})

            return render(request, "guestbook/guestbook.html", context)
