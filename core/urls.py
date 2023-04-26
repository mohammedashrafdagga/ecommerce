from .views import frontpage, register_user
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'core'

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('create-account/', register_user, name='register/'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
