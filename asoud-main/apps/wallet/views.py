from rest_framework import views, status, permissions
from rest_framework.response import Response
from utils.response import ApiResponse
from apps.wallet.models import Wallet
# Create your views here.

class WalletCheckView(views.APIView):
    def get(self, request):
        try:
            wallet = Wallet.objects.get(user=request.user)
        except Wallet.DoesNotExist:
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="Wallet Not Found",
                ), 
                status=status.HTTP_404_NOT_FOUND
            )
