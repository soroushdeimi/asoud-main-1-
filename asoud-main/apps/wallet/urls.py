from django.urls import path
from apps.wallet.views import (
    WalletBalanceView,
    WalletCheckView,
    TransactionListView
)

app_name = "wallet"


urlpatterns = [
    path(
        'balance/', 
        WalletBalanceView.as_view(), 
        name="balance"
    ),
    path(
        'balance/check/', 
        WalletCheckView.as_view(), 
        name="check"
    ),
    path(
        'transactions/', 
        TransactionListView.as_view(), 
        name="transactions"
    ),
]