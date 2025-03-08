from apps.base.admin import admin, BaseAdmin
from apps.wallet.models import Wallet

# Register your models here.

class WalletAdmin(BaseAdmin):
    list_display = ['user', 'balance']
    fields = (
        'user',
        'balance'
    ) + + BaseAdmin.fields

admin.site.register(Wallet, WalletAdmin)