# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^account/', admin.site.urls),
    url(r'^article/', include('willblog.apps.article.urls', namespace='article')),
    url(r'^collection/', include('willblog.apps.collection.urls', namespace='collection')),
    url(r'^', include('willblog.apps.index.urls', namespace='index')),
]

# urlpatterns += [
#     url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
# ]
#
# if settings.DEBUG:
#     urlpatterns = staticfiles_urlpatterns()
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
