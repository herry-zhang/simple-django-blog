# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
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
    author = models.ForeignKey(User, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    ispub = models.BooleanField(verbose_name='发布', default=True)
    views = models.IntegerField(default=1, verbose_name='浏览次数')
    description = models.TextField(blank=True, null=True, verbose_name='描述')
    url = models.URLField(null=True, verbose_name='网址')

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('collection:detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-create_time']
        verbose_name = '收集'
        verbose_name_plural = '收集'
