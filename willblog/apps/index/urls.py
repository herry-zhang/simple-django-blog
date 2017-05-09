# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
from willblog.apps.index import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', TemplateView.as_view(template_name='index/search.html'), name='search'),
]
