from django.shortcuts import render
from products.models import Product
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views import View
from django.shortcuts import get_object_or_404
# Create your views here.


@xframe_options_exempt
def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)

class ProductDetail(View):

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        context = {'product': product}
        print(product.get_absolute_url())
        return render(request, 'products/product_page.html', context)

