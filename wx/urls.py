from django.conf.urls import url
from werobot.contrib.django import make_view
from wx.robot import robot

urlpatterns = (
    url(r'^robot/$', make_view(robot)),
)
