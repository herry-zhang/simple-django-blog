# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from article.feeds import LatestArticleFeed
from article.views import *

urlpatterns = [
    url(r'^$', home, name='article'),
    url(r'(?P<pk>\d+)/$', detail, name='article_detail'),
    url(r'^feed\.xml$', LatestArticleFeed(), name='feed'),
    url(r'edit/$', article_edit, name='article_add'),
]
