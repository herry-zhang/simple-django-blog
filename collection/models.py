# coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Collection(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    category = models.CharField(max_length=50, blank=True, verbose_name='类别')
    date_time = models.DateField(auto_now_add=True, verbose_name='收集时间')
    description = models.TextField(blank=True, null=True, verbose_name='描述')
    url = models.URLField(null=True, verbose_name='网址')

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse(kwargs={'id': self.id})

    class Meta:
        ordering = ['-date_time']
        verbose_name = '收集'
        verbose_name_plural = '收集'
