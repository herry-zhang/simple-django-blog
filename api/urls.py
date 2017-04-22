from django.conf.urls import url
from api.views import *

urlpatterns = [
    url(r'^markdownedit/$', markdown_edit, name='markdownedit')
]
