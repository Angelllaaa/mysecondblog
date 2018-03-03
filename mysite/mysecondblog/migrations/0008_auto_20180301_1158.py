# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-01 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysecondblog', '0007_article_personal_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_deep_learning',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploadImage', verbose_name='PHOTO'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article_net',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploadImage', verbose_name='PHOTO'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article_python',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploadImage', verbose_name='PHOTO'),
            preserve_default=False,
        ),
    ]