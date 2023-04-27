from django.urls import path
from .views import add_to_cart, cart, checkout, hx_menu_cart, update_cart, hx_cart_total

app_name = 'cart'
urlpatterns = [
    path('', cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('checkout/', checkout, name='checkout'),
    path('update-cart/<int:product_id>/<str:action>/',
         update_cart, name='update-cart'),
    path('hx-menu-cart/', hx_menu_cart, name='hx-menu-cart'),
    path('hx-cart-total/', hx_cart_total, name='hx-cart-total'),
]
