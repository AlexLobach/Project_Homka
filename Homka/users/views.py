from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from catalog.utils import cartData
from django.contrib.auth.decorators import login_required
from catalog.models import *


def register(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            Customer.objects.create(user = form.save(), name = username, email = email )
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')