# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-15 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210515_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='correct',
            field=models.BooleanField(default='False'),
        ),
    ]
