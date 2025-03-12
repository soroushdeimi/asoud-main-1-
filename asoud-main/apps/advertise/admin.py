from apps.base.admin import admin, BaseAdmin

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'type',
        'price',
        'category'
    ]
    fields = (
        'type',
        'name',
        'description',
        'category',
        'city',
        'state',
        'email',
        'keywords',
    ) + BaseAdmin.fields
