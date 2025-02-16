from apps.base.admin import admin, BaseAdmin, BaseTabularInline

from .models import Group, Category, SubCategory

# Register your models here.


class SubCategoryTabularInline(BaseTabularInline):
    model = SubCategory

    fields = (
        'title',
        'market_fee',
        'market_slider_img',
        'market_slider_url',
    )


class CategoryAdmin(BaseAdmin):
    inlines = [
        SubCategoryTabularInline,
    ]

    list_display = [
        'title',
        'group',
    ]

    fields = (
        'group',
        'title',
        'market_fee',
        'market_slider_img',
        'market_slider_url',
    ) + BaseAdmin.fields

    readonly_fields = BaseAdmin.readonly_fields


admin.site.register(Category, CategoryAdmin)


class GroupAdmin(BaseAdmin):
    list_display = [
        'title',
    ]

    fields = (
        'title',
    ) + BaseAdmin.fields

    readonly_fields = BaseAdmin.readonly_fields


admin.site.register(Group, GroupAdmin)
