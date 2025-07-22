from apps.base.admin import admin, BaseAdmin, BaseTabularInline

from .models import (
    Product,
    ProductImage,
    ProductKeyword,
    ProductDiscount,
    ProductTheme,
    ProductCategoryGroup,
    ProductCategory,
    ProductSubCategory,
)

# Register your models here.


class ProductImageTabularInline(BaseTabularInline):
    model = ProductImage

    fields = (
        'image',
    ) + BaseTabularInline.fields

    readonly_fields = BaseTabularInline.readonly_fields


class ProductDiscountTabularInline(BaseTabularInline):
    model = ProductDiscount

    fields = (
        'position',
        'percentage',
        'duration',
        'users',
    )


class ProductAdmin(BaseAdmin):
    inlines = [
        ProductImageTabularInline,
        ProductDiscountTabularInline,
    ]

    list_display = [
        'name'
    ]

    fields = (
        'market',
        'type',
        'name',
        'description',
        'technical_detail',
        'sub_category',
        'keywords',
        'stock',
        'main_price',
        'colleague_price',
        'marketer_price',
        'maximum_sell_price',
        'status',
        'required_product',
        'gift_product',
        'is_marketer',
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


class ProductSubCategoryTabularInline(BaseTabularInline):
    model = ProductSubCategory

    fields = (
        'title',
    ) + BaseTabularInline.fields

    readonly_fields = BaseTabularInline.readonly_fields


class ProductCategoryAdmin(BaseAdmin):
    inlines = [
        ProductSubCategoryTabularInline,
    ]

    list_display = [
        'title',
        'group',
    ]

    fields = (
        'group',
        'title',
    ) + BaseAdmin.fields

    readonly_fields = BaseAdmin.readonly_fields


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductCategoryTabularInline(BaseTabularInline):
    model = ProductCategory

    fields = (
        'title',
    ) + BaseTabularInline.fields

    readonly_fields = BaseTabularInline.readonly_fields


class ProductCategoryGroupAdmin(BaseAdmin):
    inlines = [
        ProductCategoryTabularInline,
    ]

    list_display = [
        'title',
        'sub_category',
    ]

    fields = (
        'sub_category',
        'title',
    ) + BaseAdmin.fields

    readonly_fields = BaseAdmin.readonly_fields


admin.site.register(ProductCategoryGroup, ProductCategoryGroupAdmin)
