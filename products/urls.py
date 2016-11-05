from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^product/(?P<slug>[\w\-]+)/$', views.ProductDetail.as_view(), name='product_detail'),
]