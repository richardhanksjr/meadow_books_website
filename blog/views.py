from django.shortcuts import render
from django.views import View
from .models import Blog


class AllBlogs(View):

    def get(self, request):
        blogs = Blog.objects.all()
        context = {'blogs': blogs}
        return render(request, 'blog/blogs.html', context)
