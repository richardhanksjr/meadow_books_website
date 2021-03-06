# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('release_date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('slug', models.SlugField()),
                ('tpt_url', models.URLField()),
                ('blogs', models.ManyToManyField(to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('blog', models.ManyToManyField(to='blog.Blog')),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='products.Tag'),
        ),
    ]
