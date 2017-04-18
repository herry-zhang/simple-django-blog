# _*_ coding: utf-8 _*_

from django import template
import mistune
from bleach import clean
from blog.models import Category
from blog.handle.chars import summary as su

register = template.Library()


@register.filter(name='categories')
def get_categories():
    return {'categories': Category.objects.all(), }


@register.filter(name='markdown')
def md(value):
    mark = mistune.Markdown()
    return mark(clean(value))


@register.filter(name='summary')
def summary(value):
    return su(value)
