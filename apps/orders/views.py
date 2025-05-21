from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, ParcelForm
from .models import Order, Parcel
from django.contrib.auth.decorators import user_passes_test

def is_staff_user(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_staff_user)
def admin_order_list_view(request):
    """Wyświetla listę WSZYSTKICH zamówień (Order) dla administratora."""
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders/admin_order_list.html', {'orders': orders})

@login_required
def order_list_view(request):
    """
    Wyświetla listę zamówień złożonych przez zalogowanego użytkownika.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

def create_order_view(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        parcel_form = ParcelForm(request.POST)
        if order_form.is_valid() and parcel_form.is_valid():
            # Zapisujemy zamówienie
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()

            # Zapisujemy przesyłkę
            parcel = parcel_form.save(commit=False)
            parcel.order = order
            parcel.save()

            return redirect('users:profile')
    else:
        order_form = OrderForm()
        parcel_form = ParcelForm()

    return render(request, 'orders/create_order.html', {'order_form': order_form, 'parcel_form': parcel_form})
