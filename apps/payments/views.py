from django.shortcuts import render, redirect, get_object_or_404
from apps.orders.models import Order

def payment_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # sprawdź np. czy user ma prawo do płatności
    if request.method == 'POST':
        # Integracja z bramką płatności
        order.status = 'PAID'
        order.save()
        order.payment.status = 'completed'
        order.payment.save()
        return redirect('orders:order_list')

    return render(request, 'payments/payment.html', {'order': order})
