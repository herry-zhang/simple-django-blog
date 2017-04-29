# _*_ coding: utf-8 _*_

from django.conf.urls import url, include
from collection.views import *

urlpatterns = [
    url(r'^$', home, name='collection'),
    url(r'(?P<pk>\d+)/$', detail, name='collection_detail'),
]
