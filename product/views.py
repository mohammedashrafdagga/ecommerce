from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q


def shopping(request):
    products = Product.objects.all()
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')
    print(query)
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(content__icontains=query)
        )
    context = {
        'products': products,
        'categories': Category.objects.all(),
        'active_category': active_category
    }
    return render(request, 'product/shopping.html', context=context)


# detail
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/detail.html', {'product': product})
