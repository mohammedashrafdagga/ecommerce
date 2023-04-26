from django.shortcuts import render, redirect
from product.models import Product
from .forms import UserRegisterForm
from django.contrib.auth import login
# frontend page


def frontpage(request):
    products = Product.objects.all()[:8]
    return render(request, 'core/index.html', {'products': products})


def register_user(request):
    ''' Here Not needed to send form to user page - register'''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:frontpage')

    return render(request, 'core/register.html')
