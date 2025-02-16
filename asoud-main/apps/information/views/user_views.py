from rest_framework import views
from rest_framework.response import Response

from utils.response import ApiResponse

from apps.information.models import Term
from apps.information.serializers.user_serializers import TermListSerializer


class TermListAPIView(views.APIView):
    def get(self, request, format=None):
        term = Term.get_solo()

        if term is None:
            pass

        serializer = TermListSerializer(
            term,
            context={"request": request},
        )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully'
        )

        return Response(success_response)
