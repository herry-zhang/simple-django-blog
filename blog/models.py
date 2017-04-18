# _*_ coding : utf-8 _*

from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from uuslug import slugify
from bleach import clean, linkify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    collect_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=500, default="No description")
    url = models.URLField()
    views = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Article(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    writings = models.TextField()
    author = models.OneToOneField(User)
    views = models.IntegerField(default=0)
    slug = models.SlugField()
    create_date = models.DateTimeField(default=timezone.now)
    edit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class UserProfile(models.Model):
    nickname = models.CharField(max_length=18)
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to='profile_images')

    def __str__(self):
        return self.user.username
