# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 05:58
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0002_auto_20160407_0532'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='menu',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='menu_name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='header.Menu'),
        ),
    ]
