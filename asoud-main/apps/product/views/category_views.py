from rest_framework import views
from rest_framework.response import Response

from utils.response import ApiResponse

from apps.product.models import (
    ProductCategoryGroup,
    ProductCategory,
    ProductSubCategory,
)
from apps.product.serializers.category_serializers import (
    ProductCategoryGroupSerializer,
    ProductCategorySerializer,
    ProductSubCategorySerializer,
)
from apps.category.models import SubCategory


class ProductCategoryGroupListAPIView(views.APIView):
    def get(self, request, pk, format=None):
        try:
            sub_category = SubCategory.objects.get(id=pk)
        except SubCategory.DoesNotExist:
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Sub Category Not Found",
                )
            )

        group_list = ProductCategoryGroup.objects.filter(sub_category=sub_category)

        serializer = ProductCategoryGroupSerializer(
            group_list,
            many=True,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully',
        )

        return Response(success_response)


class ProductCategoryListAPIView(views.APIView):
    def get(self, request, pk, format=None):
        try:
            group_obj = ProductCategoryGroup.objects.get(id=pk)
        except ProductCategoryGroup.DoesNotExist:
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Product Category Group Not Found",
                )
            )

        category_list = ProductCategory.objects.filter(group=group_obj)

        serializer = ProductCategorySerializer(
            category_list,
            many=True,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully',
        )

        return Response(success_response)


class ProductSubCategoryListAPIView(views.APIView):
    def get(self, request, pk, format=None):
        try:
            category_obj = ProductCategory.objects.get(id=pk)
        except ProductCategory.DoesNotExist:
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Product Category Not Found",
                )
            )

        sub_category_list = ProductSubCategory.objects.filter(category=category_obj)

        serializer = ProductSubCategorySerializer(
            sub_category_list,
            many=True,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully',
        )

        return Response(success_response)
