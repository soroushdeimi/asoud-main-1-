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
        'list/<int:pk>/',
        ProductListAPIView.as_view(),
        name='list',
    ),
    path(
        'detail/<int:pk>/',
        ProductDetailAPIView.as_view(),
        name='detail',
    ),
    path(
        'theme/create/<int:pk>/',
        ProductThemeCreateAPIView.as_view(),
        name='theme-create',
    ),
    path(
        'theme/list/<int:pk>/',
        ProductThemeListAPIView.as_view(),
        name='theme-list',
    ),
    path(
        'theme/update/<int:pk>/',
        ProductThemeUpdateAPIView.as_view(),
        name='theme-update',
    ),
]
