from apps.base.admin import admin, BaseAdmin, BaseTabularInline

from .models import (
    Product,
    ProductImage,
    ProductKeyword,
    ProductDiscount,
    ProductTheme,
)

# Register your models here.


class ProductImage(BaseTabularInline):
    model = ProductImage

    fields = (
        'image',
    ) + BaseTabularInline.fields

    readonly_fields = BaseTabularInline.readonly_fields


class ProductAdmin(BaseAdmin):
    list_display = [
        'name'
    ]

    fields = (
        'market',
        'name',
        'description',
        'technical_detail',
        'keywords',
        'stock',
        'price',
        'status',
        'required_product',
        'gift_product',
        'is_marketer',
        'marketer_price',
        'tag',
        'tag_position',
        'sell_type',
        'ship_cost',
        'ship_cost_pay_type'
    ) + BaseAdmin.fields

    readonly_fields = BaseAdmin.readonly_fields


admin.site.register(Product, ProductAdmin)


class ProductKeywordAdmin(BaseAdmin):
    list_display = [
        'name',
    ]

    fields = (
        'name',
    ) + BaseAdmin.fields

    readonly_fields = BaseAdmin.readonly_fields


admin.site.register(ProductKeyword, ProductKeywordAdmin)


class ProductDiscountAdmin(BaseAdmin):
    list_display = [
        'code',
    ]

    fields = (
        'code',
        'position',
        'percentage',
        'duration',
        'users',
    ) + BaseAdmin.fields

    readonly_fields = BaseAdmin.readonly_fields


admin.site.register(ProductDiscount, ProductDiscountAdmin)


class ProductThemeAdmin(BaseAdmin):
    list_display = [
        'market',
    ]

    fields = (
        'market',
        'name',
        'order',
    ) + BaseAdmin.fields

    readonly_fields = BaseAdmin.readonly_fields


admin.site.register(ProductTheme, ProductThemeAdmin)
