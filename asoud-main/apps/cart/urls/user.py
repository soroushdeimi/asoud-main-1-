from django.urls import path
from apps.cart.views.user import (
    OrderCreateView,
    OrderListView,
    OrderDetailView,
    OrderUpdateView,
    OrderDeleteView,
)
app_name = 'user_order'

urlpatterns = [
    path('create', 
         OrderCreateView.as_view(), 
         name='order-list'
    ),
    path('list', 
         OrderListView.as_view(), 
         name='order-create'
    ),
    path('<str:pk>', 
         OrderDetailView.as_view(), 
         name='order-detail'
    ),
    path('<str:pk>/update', 
         OrderUpdateView.as_view(), 
         name='order-update'
    ),
    path('<str:pk>/delete', 
         OrderDeleteView.as_view(), 
         name='order-delete'
    ),
]