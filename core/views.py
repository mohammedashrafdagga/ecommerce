from django.shortcuts import render
from product.models import Product

# frontend page


def frontpage(request):
    products = Product.objects.all()[:8]
    return render(request, 'core/index.html', {'products': products})


def register_user(request):
    return render(request, 'core/register.html')


def login_user(request):
    return render(request, 'core/login.html')
