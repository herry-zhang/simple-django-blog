from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='分类')
    views = models.IntegerField(default=1, verbose_name='浏览次数')

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('category:detail', kwargs={'n': self.name})

    class Meta:
        ordering = ['-views']
        verbose_name = '分类'
        verbose_name_plural = '分类'
