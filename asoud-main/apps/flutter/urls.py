from django.urls import path
from apps.flutter.views import (
    MarketDetailView,
    ProductDetailView
)
app_name = 'flutter_urls'

urlpatterns = [
    path('markets', MarketDetailView.as_view(), name='market-detail'),
    path('products', ProductDetailView.as_view(), name='product-detail'),
]