# _*_ coding: utf-8 _*_

from django.conf.urls import url
from article.views import *

urlpatterns =[
    url(r'^$', home, name='article'),
    url(r'(?P<id>\d+)/$', detail, name='article_detail'),
]
