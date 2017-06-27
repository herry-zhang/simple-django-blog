from willblog.apps.article.feeds import LatestArticleFeed
from django.conf.urls import url
from willblog.apps.article import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^$', cache_page(21600)(views.index), name='index'), #cache 6h
    url(r'(?P<pk>\d+)/$', cache_page(259200)(views.detail), name='detail'), # cache 3d
    url(r'^feed\.xml$', cache_page(10800)(LatestArticleFeed()), name='feed'), # cache 3h
    # url(r'edit/$', views.edit, name='edit'),
]
