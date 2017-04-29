from datetime import datetime
from django.shortcuts import render, Http404
from handle.get_page import get_page
from .models import Article, Category


def home(request):
    posts = Article.objects.all().order_by("-pub_time")
    _dict = get_page(request, posts, 5)
    return render(request, 'article/home.html', _dict)


def detail(request, pk):
    reset = False
    visited = request.session.get('visited')
    aid = request.session.get('aid')

    if visited and aid:
        last_visit_time = datetime.strptime(visited[:-7],
                                            '%Y-%m-%d %H:%M:%S')
        if (datetime.now() - last_visit_time).seconds > 1800 and aid == pk:  #
            #  half hour
            reset = True

    else:
        reset = True
    try:
        article = Article.objects.get(id=pk)
        if reset:
            category = article.category.name
            category = Category.objects.get(name=category)
            category.views += 1
            category.save()
            article.views += 1
            article.save()
            request.session["visited"] = str(datetime.now())
            request.session['aid'] = pk
        return render(request, 'article/detail.html', {'article': article})
    except Article.DoesNotExist or Category.DoesNotExist:
        raise Http404
