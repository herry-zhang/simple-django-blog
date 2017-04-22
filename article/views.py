from django.shortcuts import render, Http404
from handle.get_page import get_page
from .models import Article


def home(request):
    posts = Article.objects.all().order_by("-date_time")
    _dict = get_page(request, posts, 5)
    return render(request, 'article/home.html', _dict)


def detail(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Http404
    else:
        return render(request, 'article/detail.html', {'article': article})
