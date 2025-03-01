from django.contrib import admin
from apps.sms.models import Line, Template, BulkSms, PatternSms
from apps.base.admin import BaseAdmin
# Register your models here.


class AdminLine(BaseAdmin):
    list_display = [
        'number',
        'is_active',
    ]

    fields = (
        'number',
        'estimated_cost',
        'is_active',
    ) + BaseAdmin.fields

admin.site.register(Line, AdminLine)


class AdminTemplate(BaseAdmin):
    list_display = [
        'template_id',
        'is_active',
    ]

    fields = (
        'template_id',
        'content',
        'variables',
        'estimated_cost',
        'is_active',
    ) + BaseAdmin.fields


admin.site.register(Template, AdminTemplate)