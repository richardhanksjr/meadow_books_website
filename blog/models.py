from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# from products.models import Tag


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True, default="musicinthemeadowbooks@gmail.com")

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)
    slug = models.SlugField(null=True)
    authors = models.ManyToManyField(Author)
    # tags = models.ManyToManyField('products.models.Tag')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

