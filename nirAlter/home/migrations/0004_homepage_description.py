# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 18:32
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
