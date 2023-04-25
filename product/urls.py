from django.urls import path
from .views import shopping, product_detail

app_name = 'product'


urlpatterns = [
    path('shopping', shopping, name='shopping'),
    path('<slug:slug>', product_detail, name='detail')
]
