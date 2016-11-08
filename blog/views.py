from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Blog


class AllBlogs(View):

    def get(self, request):
        blogs = Blog.objects.all()
        context = {'blogs': blogs}
        return render(request, 'blog/blogs.html', context)


class BlogDetail(View):

    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        context = {'blog': blog}
        return render(request, 'blog/blog_detail.html', context)