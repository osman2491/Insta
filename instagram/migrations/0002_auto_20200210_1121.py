# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-10 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_comments',
            field=models.TextField(null=True),
        ),
    ]
