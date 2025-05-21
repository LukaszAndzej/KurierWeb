from django.shortcuts import render, get_object_or_404
from apps.orders.models import Order

def track_parcel_view(request):
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number', '').strip()
        order = get_object_or_404(Order, tracking_number=tracking_number)
        parcel = order.parcel
        
        # LOG na serwerze
        print("DEBUG >> current_lat:", parcel.current_lat)
        print("DEBUG >> current_lng:", parcel.current_lng)
        
        context = {
            'order': order,
            'parcel': parcel,
        }
        return render(request, 'tracking/track_parcel.html', context)
    return render(request, 'tracking/track_parcel.html')
