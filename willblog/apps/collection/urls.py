# _*_ coding: utf-8 _*_

from django.conf.urls import url
from willblog.apps.collection import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
]
