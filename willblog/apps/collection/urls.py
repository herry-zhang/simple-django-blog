from django.conf.urls import url
from willblog.apps.collection import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^$', cache_page(21600)(views.index), name='index'),# cache 6h
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
]
