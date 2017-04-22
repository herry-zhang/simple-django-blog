# coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    author = models.ForeignKey(User, verbose_name='作者')
    category = models.CharField(max_length=50, blank=True, verbose_name='类别')
    date_time = models.DateField(auto_now_add=True, verbose_name='创建时间')
    content = models.TextField(blank=True, null=True, verbose_name='内容')

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('detail', kwargs={'id': self.id})

    class Meta:
        ordering = ['-date_time']
        verbose_name = '文章'
        verbose_name_plural = '文章'
