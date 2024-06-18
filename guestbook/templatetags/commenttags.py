from django import template

register = template.Library()

@register.filter
def in_comment(all_responses, comment):
    return all_responses.filter(comment=comment)