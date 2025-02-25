from rest_framework import serializers

from apps.category.models import Group, Category, SubCategory


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'title',
        ]


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
        ]


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            'id',
            'title',
        ]
