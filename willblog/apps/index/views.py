from django.shortcuts import render

from willblog.utils.model_get.get_popular import get_popular


def index(request):
    context = get_popular(8)
    return render(request, 'index/index.html', context)

