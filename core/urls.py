from .views import frontpage
from django.urls import path


app_name = 'core'
urlpatterns = [
    path('', frontpage, name='frontpage'),
]
