# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-16 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210515_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]
