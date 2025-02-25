from django.urls import path

from apps.category.views.user_views import GroupListAPIView, SubCategoryListAPIView, CategoryListAPIView

app_name = 'category_general'

urlpatterns = [
    path(
        'group/list/',
        GroupListAPIView.as_view(),
        name='group-list',
    ),
    path(
        'list/<str:pk>/',
        CategoryListAPIView.as_view(),
        name='category-list',
    ),
    path(
        'sub/list/<str:pk>/',
        SubCategoryListAPIView.as_view(),
        name='sub-category-list',
    ),
]
