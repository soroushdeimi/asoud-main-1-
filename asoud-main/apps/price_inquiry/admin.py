from django.contrib import admin
from apps.price_inquiry.models import (
    Inquiry,
    InquiryImage,
    InquiryAnswer
)
# Register your models here.

class InquiryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Inquiry, InquiryAdmin)


class InquiryImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(InquiryImage, InquiryImageAdmin)


class InquiryAnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(InquiryAnswer, InquiryAnswerAdmin)