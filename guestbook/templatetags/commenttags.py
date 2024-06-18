from django import template

register = template.Library()

@register.filter
def in_comment(all_responses, comment):
    return all_responses.filter(comment=comment)

@register.filter
def has_response(comment, all_responses):
    return bool(all_responses.filter(comment=comment))