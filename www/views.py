from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from utils.get_sidebar_content import get_content
from article.models import Article
from collection.models import Collection


def home(request):
    collections = Collection.objects.all().order_by('-pub_time')[:5]
    articles = Article.objects.all().order_by('-pub_time')[:5]
    context = get_content()
    context['collections'] = collections
    context['articles'] = articles
    return render(request, 'www/home.html', context)


def index(request):
    collections = Collection.objects.all().order_by('-pub_time')[:5]
    articles = Article.objects.all().order_by('-pub_time')[:5]
    context = get_content()
    context['collections'] = collections
    context['articles'] = articles
    return render(request, 'www/index.html', context)


@login_required()
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
