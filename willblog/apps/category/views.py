from datetime import datetime
from django.shortcuts import render, Http404, redirect
from willblog.apps.collection.models import Collection
from willblog.apps.category.models import Category


def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category/home.html', context)


def detail(request, n):
    try:
        category = Category.objects.get(name=n)
        articles = category.article_set.all()
        collections = category.collection_set.all()
    except Category.DoesNotExist:
        return Http404
    else:
        context = {'categories':Category.objects.all(),
                   'category':category,
                   'articles':articles,
                   'collections':collections,
                   }
        return render(request, 'category/detail.html', context)
