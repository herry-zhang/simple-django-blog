from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from article.models import Article
from collection.models import Collection


def home(request):
    collections = Collection.objects.order_by('-date_time')[:5]
    articles = Article.objects.order_by('-date_time')[:5]
    context = {'collections': collections, 'article': articles}
    return render(request, 'www/home.html', context)

@login_required()
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
