from datetime import datetime
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, Http404
from utils.get_page import get_page
from utils.get_popular import get_popular
from article.models import Article, Category
from article.forms import ArticleForm


def home(request):
    posts = Article.objects.all().order_by("-pub_time")
    context = get_page(request, posts, 8)
    return render(request, 'article/home.html', context)


def detail(request, pk):
    reset = False
    visited = request.session.get('visited')
    aid = request.session.get('aid')

    if visited and aid:
        last_visit_time = datetime.strptime(visited[:-7],
                                            '%Y-%m-%d %H:%M:%S')
        #  half hour
        if (datetime.now() - last_visit_time).seconds > 1800 and aid == pk:
            reset = True

    else:
        reset = True
    try:
        article = Article.objects.get(id=pk)
        context = get_popular()
        context["article"] = article
        if reset:
            category = article.category.name
            category = Category.objects.get(name=category)
            category.views += 1
            category.save()
            article.views += 1
            article.save()
            request.session["visited"] = str(datetime.now())
            request.session['aid'] = pk
        return render(request, 'article/detail.html', context)
    except Article.DoesNotExist or Category.DoesNotExist:
        raise Http404


@login_required()
@permission_required(("article.can_add",
                      'article.can_change',
                      'article.can_delete'
                      ))
def article_edit(request, pk=None):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, "article/success.html", context={'info': '提交成功'})
    else:
        form = ArticleForm()
    context = {"form": form}
    return render(request, "article/markdown.html", context)
