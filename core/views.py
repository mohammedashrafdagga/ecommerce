from django.shortcuts import render, redirect
from product.models import Product
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
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


@login_required
def get_profile(request):
    return render(request, 'core/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.username = request.POST.get('username')
        request.user.save()
        return redirect('core:profile')
    return render(request, 'core/edit_profile.html')
