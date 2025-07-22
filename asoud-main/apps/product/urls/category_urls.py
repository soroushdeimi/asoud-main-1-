from django.urls import path

from apps.product.views.category_views import (
    ProductCategoryGroupListAPIView,
    ProductCategoryListAPIView,
    ProductSubCategoryListAPIView,
)

app_name = 'product_category'

urlpatterns = [
    path(
        'group/list/<str:pk>/',
        ProductCategoryGroupListAPIView.as_view(),
        name='group-list',
    ),
    path(
        'list/<str:pk>/',
        ProductCategoryListAPIView.as_view(),
        name='category-list',
    ),
    path(
        'sub/list/<str:pk>/',
        ProductSubCategoryListAPIView.as_view(),
        name='sub-category-list',
    ),
]
