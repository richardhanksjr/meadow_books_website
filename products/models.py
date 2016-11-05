from __future__ import unicode_literals

from django.db import models
from blog.models import Blog, Author
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    release_date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField()
    tpt_url = models.URLField()
    # tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField(Author)
    tags = models.ManyToManyField('Tag')
    preview_url = models.CharField(max_length=200, null=True, default=None)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title



