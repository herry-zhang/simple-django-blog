from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from utils.get_popular import get_popular


def index(request):
    context = get_popular(8)
    return render(request, 'www/index.html', context)


@login_required()
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
