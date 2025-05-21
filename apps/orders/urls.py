from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list_view, name='order_list'),
    path('create/', views.create_order_view, name='create_order'),
    path('admin/list/', views.admin_order_list_view, name='admin_order_list')
]
