from django import template
from guestbook.models import Comment

register = template.Library()

@register.filter
def in_comment(all_responses, comment):

    return all_responses.filter(comment=comment)

@register.filter
def has_response(comment):
    return bool(Comment.objects.filter(comment=comment))