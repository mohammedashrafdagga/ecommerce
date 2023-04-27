from django.shortcuts import redirect
from .models import Order, OrderItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


@login_required
def start_ordering(request):
    cart = Cart()
    if request.method == 'POST':
        form = OrderForm(request.POST, user=request.user)
        order = form.save()
        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item = OrderItem.objects.create(
                order=order, product=product, price=price, quantity=quantity)
        return redirect('core:profile')
    return redirect('cart:cart')
