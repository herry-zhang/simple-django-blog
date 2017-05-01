# _*_ coding: utf-8 _*_
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from www.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'index', index, name="index"),
    url(r'^logout/$', logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls'), name='search'),
    url(r'^article/', include('article.urls')),
    url(r'^collection/', include('collection.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
