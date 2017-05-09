# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='分类')),
                ('views', models.IntegerField(default=1, verbose_name='浏览次数')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['-views'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('ispub', models.BooleanField(default=True, verbose_name='发布')),
                ('views', models.IntegerField(default=1, verbose_name='浏览次数')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('url', models.URLField(null=True, verbose_name='网址')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Category')),
            ],
            options={
                'verbose_name': '收集',
                'verbose_name_plural': '收集',
                'ordering': ['-create_time'],
            },
        ),
    ]
