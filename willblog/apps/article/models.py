# coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='分类')
    views = models.IntegerField(default=1, verbose_name='浏览次数')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-views']
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    author = models.ForeignKey(User, verbose_name='作者')
    category = models.ForeignKey(Category)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    ispub = models.BooleanField(verbose_name='发布', default=True)
    views = models.IntegerField(default=1, verbose_name='浏览次数')
    content = models.TextField(blank=True, null=True, verbose_name='内容')

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("article:detail", kwargs={'pk': self.id})

    class Meta:
        ordering = ['-create_time']
        verbose_name = '文章'
        verbose_name_plural = '文章'
