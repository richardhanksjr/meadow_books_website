from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.AllBlogs.as_view(), name='all_blogs'),
    url(r'^blog/(?P<slug>[\w\-]+)/$', views.BlogDetail.as_view(), name='blog_detail'),
]
