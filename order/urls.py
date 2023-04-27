from django.urls import path
from .views import start_ordering

app_name = 'order'
urlpatterns = [
    path('star-order/', start_ordering, name='start-order'),
]
