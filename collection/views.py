from datetime import datetime
from django.shortcuts import render, Http404, redirect
from handle.get_page import get_page
from collection.models import Collection, Category


def home(request):
    posts = Collection.objects.all().order_by("-date_time")
    _dict = get_page(request, posts, 5)
    return render(request, 'collection/home.html', _dict)


def detail(request, id):
    reset = False
    visited = request.session.get('visited')
    cid = request.session.get('cid')

    if visited and cid:
        last_visit_time = datetime.strptime(visited[:-7],
                                            '%Y-%m-%d %H:%M:%S')
        if (datetime.now() - last_visit_time).seconds > 1800 and cid == id:  # half hour
            reset = True

    else:
        reset = True
    try:
        collection = Collection.objects.get(id=id)
        if reset:
            category = collection.category.name
            category = Category.objects.get(name=category)
            category.views += 1
            category.save()
            collection.views += 1
            collection.save()
            request.session["visited"] = str(datetime.now())
            request.session['aid'] = id
        return redirect(collection.url)
    except Collection.DoesNotExist or Category.DoesNotExist:
        raise Http404
