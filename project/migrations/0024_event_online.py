# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-19 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0023_group_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
