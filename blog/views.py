# _*_ coding:utf-8 _*_

from datetime import datetime
from jieba import cut
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, Http404
from blog.handle.markdown import md2html
from blog.handle.image import thumbnail
from blog.handle.chars import user_check
from .forms import *


def time_in_visit(request):
    reset_last_visit_time = False
    visits = request.session.get('visits')
    last_visit = request.session.get('last_visit')
    if not visits:
        visits = 1
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7],
                                            '%Y-%m-%d %H:%M:%S')
        if (datetime.now() - last_visit_time).seconds > 10:
            visits += 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True
    if reset_last_visit_time:
        request.session[last_visit] = str(datetime.now())
        request.session['visits'] = visits
    return {'visits': visits, 'last_visit': request.session[last_visit]}


def index(request, template='blog/index/index.html'):
    context = time_in_visit(request)
    categories = Category.objects.order_by('-views')[:10]  # "-"代表降序排列
    pages = Page.objects.order_by('-views')[:10]
    articles = Article.objects.order_by('-views')[:10]
    context['categories'] = categories
    context['pages'] = pages
    context['articles'] = articles
    return render(request, template, context)


def search(request, template='blog/index/index.html'):
    finds = []
    results = False
    try:
        sorts = request.GET['search']
        sorts = cut(sorts)
        for sort in sorts:
            finds += Article.objects.filter(title__icontains=sort)
            finds = list(set(finds))
        if not finds:
            results = True
    except Exception:
        pass
    return render(request, template, {'finds': finds, 'results': results})


def about(request, template='blog/index/index.html'):
    context = time_in_visit(request)
    context['username'] = request.user
    return render(request, template, context)


def contact_me(request, template='blog/index/index.html'):
    render(request, template, {})


def page(request, template='blog/index.html', category=False):
    categories = Category.objects.all()
    context = {'categories': categories, }
    if category:
        try:
            category = Category.objects.get(slug=category)
            pages = Page.objects.filter(category=category)
        except Category.DoesNotExist:
            raise Http404("Category does not exist!")
    else:
        pages = Page.objects.all()
    context['pages'] = pages
    return render(request, template, context)


def article(request, writings=None, template='blog/index.html', category=False):
    if writings:
        try:
            writing = Article.objects.get(slug=writings)
            writing.views += 1
            writing.save()
            articles = Article.objects.order_by("-views")[:10]
            context = {'article': writing, "articles": articles}
            return render(request, template, context)
        except Article.DoesNotExist:
            raise Http404({'errors': "Article can't find"})
    else:
        categories = Category.objects.all()
        context = {'categories': categories, }
        if category:
            try:
                category = Category.objects.get(slug=category)
                articles = Article.objects.filter(category=category)
            except Category.DoesNotExist:
                raise Http404({'errors': "Category does not exist!"})
        else:
            articles = Article.objects.all()
        context['articles'] = articles
        return render(request, template, context)


@login_required()
@permission_required('blog.Category.Can_add_category')
def add_category(request, template='blog/index/index.html'):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        redirect_url = '/'
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(redirect_url)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, template, {'form': form})


@login_required()
def add_page(request, template='blog/index/index.html'):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid and request.POST.get('category'):
            cat = request.POST['category']
            pages = form.save(commit=False)
            category = Category.objects.get(slug=cat)
            pages.category = category
            pages.views = 0
            pages.save()
            redirect_url = '/category/{0}'.format(category.slug)
            return HttpResponseRedirect(redirect_url)
        else:
            raise Http404({'form_errors': form.errors, })
    else:
        form = PageForm()
    categories = Category.objects.all()
    content_dict = {'form': form, 'categories': categories}
    return render(request, template, content_dict)


@login_required()
def add_article(request, template='blog/index/index.html'):
    content = {'categories': Category.objects.all(), }
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid() and request.POST.get('category'):
            articles = form.save(commit=False)
            category = Category.objects.get(slug=request.POST['category'])
            articles.category = category
            articles.views = 0
            articles.author = User.objects.get(username=request.user)
            articles.save()
            redirect_url = '/'
            return HttpResponseRedirect(redirect_url)
        else:
            raise Http404({'form_error': form.errors})
    else:
        form = ArticleForm()
    content['form'] = form
    return render(request, template, content)


@login_required()
def pre_markdown(request, template='404.html'):
    if request.method == 'POST':
        writings = md2html(request.POST['writings'])
        content = {'writings': writings, }
        return render(request, template, content)
    else:
        return render(request, template)


def register(request, template='blog/index/index.html'):
    registered = False
    if request.method == 'POST':
        if not request.POST['nickname']:
            request.POST['nickname'] = request.POST['username']
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid() and user_check(
                request.POST.get("username"),
                request.POST.get("password"),
                request.POST['nickname']):
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            if 'photo' in request.FILES:
                thumbnail(request.FILES('picture')).save('', "JPEG")
                profile.picture = request.FILES('photo')
            profile.save()
            registered = True
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
        else:
            return Http404
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, template,
                  {'user_form': user_form, 'profile_form': profile_form,
                   'registered': registered})


def user_login(request, template='blog/index/index.html',
               loginFalse='blog/index/index.html'):
    if request.user.is_authenticated():
        return HttpResponse('您已登陆，不需要重复登陆。')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, loginFalse, {})
    else:
        return render(request, template, {})


@login_required()
def user_logout(request, redirect='/'):
    logout(request)
    return HttpResponseRedirect(redirect)


@login_required()
def user_profile(request, template='404.html'):
    context = time_in_visit(request)
    users = User.objects.get(username=request.user.username)
    user_profiles = UserProfile.objects.get(user=users)
    context['user'] = users
    context['profile'] = user_profiles
    return render(request, template, context)
