from rest_framework import serializers
from django.urls import reverse

from apps.product.models import (
    Product,
    ProductTheme,
)


class ProductCreateSerializer(serializers.ModelSerializer):
    # TODO: keywords

    class Meta:
        model = Product
        fields = [
            'market',
            'name',
            'description',
            'technical_detail',
            'stock',
            'price',
            'status',
            'required_product',
            'gift_product',
            'is_marketer',
            'marketer_price',
            'sell_type',
            'ship_cost',
            'ship_cost_pay_type',
        ]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'technical_detail',
            # 'keywords' TODO: Handle manytomanyfield
            'stock',
            'price',
            # 'required_product', TODO: Handle foreignkey
            # 'gift_product', TODO: Handle foreignkey
            'is_marketer'
            'marketer_price',
            'tag',
            'tag_position',
            'sell_type',
            'ship_cost',
            'ship_cost_pay_type',
            # 'comments', TODO: Handle GenericRelation
            # TODO: Handle ProductImage, ProductDiscount
        ]


class ProductThemeListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = ProductTheme
        fields = [
            'id',
            'name',
            'order',
            'products',
        ]

    def get_products(self, obj):
        products = obj.products.all()
        return ProductListSerializer(products, many=True, context=self.context).data


class ProductThemeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTheme
        fields = [
            'name',
            'order',
        ]
