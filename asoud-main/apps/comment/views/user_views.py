from rest_framework import views, status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from utils.response import ApiResponse

from apps.comment.serializers.user_serializers import (
    CommentCreateSerializer,
    CommentListSerializer,
)

from apps.comment.models import Comment


class CommentCreateAPIView(views.APIView):
    def post(self, request):
        serializer = CommentCreateSerializer(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid(raise_exception=True):
            comment = serializer.save(
                creator=self.request.user,
            )

            comment_id = comment.id

            success_response = ApiResponse(
                success=True,
                code=200,
                data={
                    'comment': comment_id,
                    **serializer.data,
                },
                message='Comment created successfully.',
            )

            return Response(success_response, status=status.HTTP_201_CREATED)


class CommentListAPIView(views.APIView):
    def get(self, request):
        # Get content type and object ID from query parameters
        content_type = self.request.query_params.get('content_type')
        object_id = self.request.query_params.get('object_id')

        if not content_type or not object_id:
            raise ApiResponse(
                success=False,
                code=500,
                error={
                    'code': 'server_error',
                    'detail': 'Server error',
                }
            )

        # Get the actual content type model
        try:
            content_type_instance = ContentType.objects.get(
                model=content_type,
            )

            comment_list = Comment.objects.filter(
                content_type=content_type_instance,
                object_id=object_id,
            )

            serializer = CommentListSerializer(
                comment_list,
                many=True,
                context={"request": request},
            )

            success_response = ApiResponse(
                success=True,
                code=200,
                data=serializer.data,
                message='Comment retrieved successfully.',
            )

            return Response(success_response)

        except ContentType.DoesNotExist:
            raise ApiResponse(
                success=False,
                code=500,
                error={
                    'code': 'server_error',
                    'detail': 'Server error',
                }
            )
