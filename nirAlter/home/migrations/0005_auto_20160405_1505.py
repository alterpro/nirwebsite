# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='description',
        ),
        migrations.AddField(
            model_name='homepage',
            name='top_sub_title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homepage',
            name='top_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
