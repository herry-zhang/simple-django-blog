from django.shortcuts import render, Http404, redirect
from handle.get_page import get_page
from .models import Collection


def home(request):
    posts = Collection.objects.all().order_by("-date_time")
    _dict = get_page(request, posts, 5)
    return render(request, 'collection/home.html', _dict)


def detail(request, id):
    try:
        collection = Collection.objects.get(id=id)
    except Collection.DoesNotExist:
        return Http404
    else:
        return redirect(collection.url)
