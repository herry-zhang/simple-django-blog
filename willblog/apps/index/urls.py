from django.conf.urls import url
from django.views.generic import TemplateView
from willblog.apps.index import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^$', cache_page(21600)(views.index), name='index'),# 6h = 60*60*6 = 21600
    url(r'^search/$', TemplateView.as_view(template_name='index/search.html'), name='search'),
]
