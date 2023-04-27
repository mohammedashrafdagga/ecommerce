from django.urls import path
from .views import add_to_cart, cart, checkout

app_name = 'cart'
urlpatterns = [
    path('', cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('checkout/', checkout, name='checkout'),
]
