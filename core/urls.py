from .views import frontpage, register_user, login_user
from django.urls import path


app_name = 'core'
urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('create-account/', register_user, name='register/'),
    path('login', login_user, name='login')
]
