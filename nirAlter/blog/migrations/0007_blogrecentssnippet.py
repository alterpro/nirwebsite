# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160407_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogRecentsSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text=b'the title will be displayed on the page', max_length=255)),
                ('display_count', models.IntegerField(help_text=b'number of posts to be displayed')),
            ],
        ),
    ]
