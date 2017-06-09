from django.conf.urls import url
from willblog.apps.category import views

urlpatterns = [
    url(r'^$',views.index, name='home'),
    url(r'(?P<n>\w+)/$', views.detail, name='detail'),
]
