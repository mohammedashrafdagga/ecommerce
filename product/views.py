from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def shopping(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product/shopping.html', {'products': products, 'categories': categories})


# detail
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/detail.html', {'product': product})
