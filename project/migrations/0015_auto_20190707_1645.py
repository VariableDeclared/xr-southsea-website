# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-07 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20190707_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpluginmodel',
            name='show_category_filters',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='gallery',
            field=models.BooleanField(default=True, help_text='Pull in all images that are in the same folder as the article image and display as a gallery'),
        ),
    ]
