# coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='分类')
    views = models.IntegerField(default=1, verbose_name='浏览次数')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-views']
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Collection(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    category = models.ForeignKey(Category)
    date_time = models.DateField(auto_now_add=True, verbose_name='收集时间')
    views = models.IntegerField(default=1, verbose_name='浏览次数')
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
