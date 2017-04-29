from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from article.models import Article
from collection.models import Collection


def home(request):
    collections = Collection.objects.all().order_by('-pub_time')[:5]
    articles = Article.objects.all().order_by('-pub_time')[:5]
    context = {'collections': collections, 'articles': articles}
    return render(request, 'www/home.html', context)


@login_required()
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
