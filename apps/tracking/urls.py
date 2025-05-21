from django.urls import path
from . import views

app_name = 'tracking'

urlpatterns = [
    path('', views.track_parcel_view, name='track_parcel'),
]
