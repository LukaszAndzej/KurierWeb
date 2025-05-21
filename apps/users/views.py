from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from apps.orders.models import Order 

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatyczne logowanie po rejestracji
            return redirect('users:profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:profile')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('users:login')

@login_required
def profile_view(request):
    # Statystyki użytkownika
    user_orders = Order.objects.filter(user=request.user)
    stats = {
        'total_orders': user_orders.count(),
        'pending_orders': user_orders.filter(status='NEW').count(),
        'delivered_orders': user_orders.filter(status='DELIVERED').count(),
    }
    return render(request, 'users/profile.html', {'stats': stats})
