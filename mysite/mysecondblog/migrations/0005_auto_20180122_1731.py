# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-22 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysecondblog', '0004_auto_20180122_1651'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='article_deep_learning',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article_net',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article_python',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
