from rest_framework import serializers
from django.urls import reverse
import jdatetime

from apps.market.models import (
    Market,
    MarketReport,
)


class MarketListSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    sub_category_title = serializers.SerializerMethodField()
    view_count = serializers.SerializerMethodField()

    # theme = MarketThemeCreateSerializer()

    class Meta:
        model = Market
        fields = [
            'id',
            'business_id',
            'name',
            'sub_category',
            'sub_category_title',
            'status',
            'is_paid',
            'created_at',
            'logo_img',
            'background_img',
            # 'theme',
            'view_count',
        ]

    def get_created_at(self, obj):
        created_at_date = obj.created_at.date()
        jalali_date = jdatetime.date.fromgregorian(date=created_at_date)
        return jalali_date.strftime("%Y/%m/%d")

    def get_sub_category_title(self, obj):
        return obj.sub_category.title if obj.sub_category else None

    def get_view_count(self, obj):
        market_viewed_by = obj.viewed_by.all()
        return market_viewed_by.count()


class MarketReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketReport
        fields = [
            'description',
        ]
