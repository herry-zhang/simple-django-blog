# _*_ coding: utf-8 _*_

from django.conf.urls import url
from article.feeds import LatestArticleFeed
from article.views import *

urlpatterns = [
    url(r'^$', home, name='article'),
    url(r'(?P<id>\d+)/$', detail, name='article_detail'),
    url(r'^feed/$', LatestArticleFeed(), name='feed'),
]
