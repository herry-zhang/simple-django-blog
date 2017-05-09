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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('ispub', models.BooleanField(default=True, verbose_name='发布')),
                ('views', models.IntegerField(default=1, verbose_name='浏览次数')),
                ('content', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-create_time'],
            },
        ),
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
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Category'),
        ),
    ]
