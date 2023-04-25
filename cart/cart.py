from django.conf import settings
from product.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    # using to add item in cart session
    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()

    # remove
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    # to iter all item in cart session

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

    # return all quantity in cart session
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # to save item in cart session
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
