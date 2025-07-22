from rest_framework import views
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

from utils.response import ApiResponse

from apps.information.models import Term
from apps.information.serializers.user_serializers import TermListSerializer


class TermListAPIView(views.APIView):
    def get(self, request, format=None):
        try:
            term = Term.get_solo()
        except Exception as e:
            logger.exception("Failed to retrieve Term: %s", e)
            return Response(
                ApiResponse(
                    success=False,
                    code=404,
                    error="No Term Found"
            )
        )

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
