import time
import math
from geopy.distance import geodesic
from django.conf import settings
from apps.orders.models import Order


def find_nearest_sorting_center(lat, lng):
    """Zwraca obiekt z settings.SORTING_CENTERS najbliższy współrzędnym (lat, lng)."""
    nearest = None
    min_distance = float('inf')

    for center in settings.SORTING_CENTERS:
        dist = geodesic((lat, lng), (center['lat'], center['lng'])).km
        # dist = haversine_distance(lat, lng, center['lat'], center['lng'])
        if dist < min_distance:
            min_distance = dist
            nearest = center

    return nearest

def update_order_status():
    while True:
        orders = Order.objects.filter(status__in=[
            'NEW', 'PICKED_UP', 'SORTING', 'OUT_FOR_DELIVERY'
        ])
        for order in orders:
            parcel = getattr(order, 'parcel', None)
            if not parcel:
                continue  # Bez przesyłki nie ma co aktualizować

            if order.status == 'NEW':
                # Zmiana statusu z NEW -> PICKED_UP
                order.status = 'PICKED_UP'
                # Znajdź w settings.py obiekt odpowiadający parcel.pickup_point
                pickup_config = next((p for p in settings.PICKUP_LOCATIONS
                                      if p['key'] == parcel.pickup_point), None)
                if pickup_config:
                    parcel.current_lat = pickup_config['lat']
                    parcel.current_lng = pickup_config['lng']
                parcel.save()

            elif order.status == 'PICKED_UP':
                order.status = 'SORTING'
                # Pobieramy najbliższą sortownię na podstawie docelowych współrzędnych paczki
                if parcel.recipient_coordinates:
                    rec_lat = parcel.recipient_coordinates.get('lat')
                    rec_lng = parcel.recipient_coordinates.get('lng')
                    center = find_nearest_sorting_center(rec_lat, rec_lng)
                    parcel.current_lat = center['lat']
                    parcel.current_lng = center['lng']
                    parcel.save()

            elif order.status == 'SORTING':
                order.status = 'OUT_FOR_DELIVERY'
                # Ustawiamy współrzędne docelowe (odbiorca)
                if parcel.recipient_coordinates:
                    parcel.current_lat = parcel.recipient_coordinates.get('lat')
                    parcel.current_lng = parcel.recipient_coordinates.get('lng')
                parcel.save()

            elif order.status == 'OUT_FOR_DELIVERY':
                order.status = 'DELIVERED'
                # Paczka dostarczona. Koordynaty już są docelowe.

            order.save()
        time.sleep(60)  # co minutę
