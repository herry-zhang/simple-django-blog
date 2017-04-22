# _*_ coding: utf-8 _*_

from django.conf.urls import url
from collection.views import *

urlpatterns = [
    url(r'^$', home, name='collection'),
    url(r'(?P<id>\d+)/$', detail, name='collection_detail'),
]
