from apps.wallet.models import Wallet
from django.db import transaction

class WalletCore:

    @staticmethod
    def increase_balance(pk:str, amount:float):
        if amount <= 0:
            return False, "Invalid amount"
        
        try:
            wallet = Wallet.objects.get(id=pk)
        except Exception as e:
            return False, str(e)

        with transaction.atomic():
            wallet.balance += amount

            wallet.save()
        
        return True, wallet.balance
    
    @staticmethod
    def decrease_balance(pk:str, amount:float):
        if amount <= 0:
            return False, "Invalid amount"
        
        try:
            wallet = Wallet.objects.get(id=pk)
        except Exception as e:
            return False, str(e)

        if wallet.balance < amount:
            return False, "Insufficient Balance"
        
        with transaction.atomic():
            wallet.balance -= amount

            wallet.save()
        
        return True, wallet.balance
    
    @staticmethod
    def transaction(from_pk:str, to_pk:str, amount: float):
        if amount <= 0:
            return False, "Invalid amount"
        
        try:
            from_wallet = Wallet.objects.get(id=from_pk)
            to_wallet = Wallet.objects.get(id=to_pk)
        except Exception as e:
            return False, str(e)

        if from_wallet.balance < amount:
            return False, "Insufficient Balance"
        
        with transaction.atomic():
            from_wallet.balance -= amount
            to_wallet.balance += amount

            from_wallet.save()
            to_wallet.save()
        
        return True, (from_wallet.balance, to_wallet.balance)

