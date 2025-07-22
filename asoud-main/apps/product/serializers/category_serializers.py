from rest_framework import serializers

from apps.product.models import (
    ProductCategoryGroup,
    ProductCategory,
    ProductSubCategory,
)


class ProductCategoryGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryGroup
        fields = [
            'id',
            'title',
        ]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'title',
        ]


class ProductSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCategory
        fields = [
            'id',
            'title',
        ]
