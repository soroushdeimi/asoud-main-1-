from django.urls import path

from apps.product.views.owner_views import (
    ProductCreateAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ProductThemeCreateAPIView,
    ProductThemeListAPIView,
    ProductThemeUpdateAPIView,
)

app_name = 'product_owner'

urlpatterns = [
    path(
        'create/',
        ProductCreateAPIView.as_view(),
        name='create',
    ),
    path(
        'list/<str:pk>/',
        ProductListAPIView.as_view(),
        name='list',
    ),
    path(
        'detail/<str:pk>/',
        ProductDetailAPIView.as_view(),
        name='detail',
    ),
    path(
        'theme/create/<str:pk>/',
        ProductThemeCreateAPIView.as_view(),
        name='theme-create',
    ),
    path(
        'theme/list/<str:pk>/',
        ProductThemeListAPIView.as_view(),
        name='theme-list',
    ),
    path(
        'theme/update/<str:pk>/',
        ProductThemeUpdateAPIView.as_view(),
        name='theme-update',
    ),
]
