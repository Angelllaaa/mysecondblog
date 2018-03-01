# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-22 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysecondblog', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_net',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Article_personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=5000)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Article_python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=5000)),
            ],
        ),
        migrations.RenameModel(
            old_name='Article',
            new_name='Article_deep_learning',
        ),
    ]
