from django.urls import path

from apps.region.views.user_views import CountryListAPIView, ProvinceListAPIView, CityListAPIView

app_name = 'region_general'

urlpatterns = [
    path(
        'country/list/',
        CountryListAPIView.as_view(),
        name='country-list',
    ),
    path(
        'province/list/<int:pk>/',
        ProvinceListAPIView.as_view(),
        name='province-list',
    ),
    path(
        'city/list/<int:pk>/',
        CityListAPIView.as_view(),
        name='city-list',
    ),
]
