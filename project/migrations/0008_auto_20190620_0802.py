# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 08:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20190619_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='promote',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.Category'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_image', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
