from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('create/', views.create_ticket_view, name='create_ticket'),
    path('list/', views.ticket_list_view, name='ticket_list'),
    path('admin/list/', views.admin_ticket_list_view, name='admin_ticket_list'),
    path('admin/resolve/<int:ticket_id>/', views.admin_resolve_ticket_view, name='admin_resolve_ticket'),
    path('my_list/', views.my_ticket_list_view, name='my_ticket_list'),
]
