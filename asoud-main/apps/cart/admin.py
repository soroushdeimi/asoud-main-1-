from apps.base.admin import admin, BaseAdmin, BaseTabularInline

from apps.cart.models import Cart, CartItem, CartPayment

# Register your models here.


class CartItemTabularInlune(BaseTabularInline):
    model = CartItem
    extra = 0

    fields = (
        'product',
        'quantity',
        'total_price',
    ) + BaseTabularInline.fields

    readonly_fields = (
        'total_price',
    ) + BaseTabularInline.readonly_fields

    def total_price(self, obj):
        return obj.total_price()
    total_price.short_description = 'Total price'


class CartAdmin(BaseAdmin):
    inlines = [
        CartItemTabularInlune,
    ]

    list_display = [
        'user',
        'total_price',
        'total_items',
        'description',
    ]

    fields = (
        'user',
        'total_price',
        'total_items',
        'description',
    ) + BaseAdmin.fields

    readonly_fields = (
        'total_price',
        'total_items',
    ) + BaseAdmin.readonly_fields

    def total_price(self, obj):
        return obj.total_price()
    total_price.short_description = 'Total price'

    def total_items(self, obj):
        return obj.total_items()
    total_items.short_description = 'Total items'


admin.site.register(Cart, CartAdmin)


class CartPaymentAdmin(BaseAdmin):
    list_display = [
        'cart',
        'type',
        'status',
        'amount',
    ]

    fields = (
        'cart',
        'type',
        'status',
        'amount',
    ) + BaseAdmin.fields

    readonly_fields = BaseAdmin.readonly_fields


admin.site.register(CartPayment, CartPaymentAdmin)
