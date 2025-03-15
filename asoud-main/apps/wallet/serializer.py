from rest_framework import serializers
from apps.wallet.models import Wallet, Transaction


class WalletCheckSerializer(serializers.Serializer):
    amount = serializers.CharField()

class WalletSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Wallet
        fields = [
            'id',
            'balance',
        ]

class TransactionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    from_wallet = WalletSerializer()
    to_wallet = WalletSerializer()
    class Meta:
        model = Transaction
        fields = [
            'id',
            'from_wallet',
            'to_wallet',
            'action',
            'amount',
            'created_at',
        ]