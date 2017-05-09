# _*_ coding: utf-8 _*_

from willblog.apps.article.feeds import LatestArticleFeed
from django.conf.urls import url

from willblog.apps.article import views

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^feed\.xml$', LatestArticleFeed(), name='feed'),
    # url(r'edit/$', views.edit, name='edit'),
]
