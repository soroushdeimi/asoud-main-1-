from django.urls import path

from apps.market.views.user_views import (
    MarketListAPIView,
    MarketReportAPIView,
    MarketBookmarkAPIView,
)

app_name = 'market_user'

urlpatterns = [
    path(
        'list/',
        MarketListAPIView.as_view(),
        name='list',
    ),
    path(
        'report/<int:pk>/',
        MarketReportAPIView.as_view(),
        name='report',
    ),
    path(
        'bookmark/',
        MarketBookmarkAPIView.as_view(),
        name='bookmark',
    ),
    path(
        'bookmark/<int:pk>/',
        MarketBookmarkAPIView.as_view(),
        name='bookmark',
    ),
]
