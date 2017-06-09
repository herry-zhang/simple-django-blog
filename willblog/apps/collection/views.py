from datetime import datetime
from django.shortcuts import render, Http404, redirect
from willblog.apps.collection.models import Collection
from willblog.apps.category.models import Category
from willblog.utils.model_get.get_page import get_page


def index(request):
    posts = Collection.objects.order_by("-create_time")
    context = get_page(request, posts, 8)
    return render(request, 'collection/index.html', context)


def detail(request, pk):
    reset = False
    visited = request.session.get('visited')
    cid = request.session.get('cid')

    if visited and cid:
        last_visit_time = datetime.strptime(visited[:-7],
                                            '%Y-%m-%d %H:%M:%S')
        if (datetime.now() - last_visit_time).seconds > 1800 and cid == pk:  #
            #  half hour
            reset = True

    else:
        reset = True
    try:
        collection = Collection.objects.get(id=pk)
        if reset:
            category = collection.category.name
            category = Category.objects.get(name=category)
            category.views += 1
            category.save()
            collection.views += 1
            collection.save()
            request.session["visited"] = str(datetime.now())
            request.session['cid'] = pk
        return redirect(collection.url)
    except Collection.DoesNotExist or Category.DoesNotExist:
        raise Http404
