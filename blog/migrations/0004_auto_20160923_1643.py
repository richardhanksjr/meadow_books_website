# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160923_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(default='musicinthemeadowbooks@gmail.com', max_length=254, null=True),
        ),
    ]