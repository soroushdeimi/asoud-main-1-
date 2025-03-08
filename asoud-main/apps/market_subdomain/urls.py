from django.urls import path
from apps.market_subdomain.views import (
    MarketDetailView,
    ProductDetailView
)


app_name = 'subdomains'

urlpatterns = [
    path(
        '',
        MarketDetailView.as_view()
    ),
    path(
        '/product',
        ProductDetailView.as_view()
    ),
]