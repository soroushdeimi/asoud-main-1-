from rest_framework import views
from rest_framework.response import Response
import logging
logger = logging.getLogger(__name__)

from utils.response import ApiResponse

from apps.region.models import Country, Province, City
from apps.region.serializers.user_serializers import CountryListSerializer, ProvinceListSerializer, CityListSerializer


class CountryListAPIView(views.APIView):
    def get(self, request, format=None):
        country_list = Country.objects.all()

        serializer = CountryListSerializer(
            country_list,
            many=True,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully'
        )

        return Response(success_response)


class ProvinceListAPIView(views.APIView):
    def get(self, request, pk, format=None):
        try:
            country_obj = Country.objects.get(id=pk)
        except Country.DoesNotExist:
            logger.exception("Country not found: %s", pk)
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Country Not Found"
                )
            )
        
        province_list = Province.objects.filter(country=country_obj)

        serializer = ProvinceListSerializer(
            province_list,
            many=True,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully'
        )

        return Response(success_response)


class CityListAPIView(views.APIView):
    def get(self, request, pk, format=None):
        try:
            province_obj = Province.objects.get(id=pk)
        except Province.DoesNotExist:
            logger.exception("Province not found: %s", pk)
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Province Not Found"
                )
            )
        
        city_list = City.objects.filter(province=province_obj)

        serializer = CityListSerializer(
            city_list,
            many=True,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully'
        )

        return Response(success_response)
