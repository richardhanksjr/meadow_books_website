# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160923_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='products',
        ),
    ]
