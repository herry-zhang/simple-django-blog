from django import template
from django.utils.safestring import mark_safe
from mistune import markdown

register = template.Library()


@register.filter(name="mk")
def mk(value):
    return mark_safe(markdown(value))
