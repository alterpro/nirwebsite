# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('header', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='menu',
            managers=[
                ('menu_items', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='parent_menu',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='link_external',
            field=models.URLField(blank=True, null=True, verbose_name='External link'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='parent',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_links', to='header.Menu'),
        ),
    ]