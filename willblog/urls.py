# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^account/', admin.site.urls),
    url(r'^article/',
        include('willblog.apps.article.urls', namespace='article')),
    url(r'^collection/',
        include('willblog.apps.collection.urls', namespace='collection')),
    url(r'category/',
        include('willblog.apps.category.urls', namespace='category')),
    url(r'^', include('willblog.apps.index.urls', namespace='index')),
]

