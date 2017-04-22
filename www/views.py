from django.shortcuts import render
from article.models import Article
from collection.models import Collection


def home(request):
    collections = Collection.objects.order_by('-date_time')[:5]
    articles = Article.objects.order_by('-date_time')[:5]
    context = {'collections': collections, 'articles': articles}
    return render(request, 'www/home.html', context)

