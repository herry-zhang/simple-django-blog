import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="mk")
def mk(value):
    return mark_safe(markdown.markdown(value))
