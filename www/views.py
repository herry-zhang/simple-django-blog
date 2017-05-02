from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from utils.get_sidebar_content import get_sidebar_content


def home(request):
    context = get_sidebar_content()
    return render(request, 'www/home.html', context)


def index(request):
    context = get_sidebar_content()
    return render(request, 'www/index.html', context)


@login_required()
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
