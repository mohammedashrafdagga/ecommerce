from django.urls import path
from .views import start_ordering

app_name = 'order'
urlpatterns = [
    path('star_ordering/', start_ordering, name='start_ordering'),
]
