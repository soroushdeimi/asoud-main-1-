from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from apps.comment.models import Comment
from apps.market.models import Market

from apps.market.serializers.user_serializers import MarketListSerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(write_only=True)  # market or product
    object_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = [
            'content',
            'parent_comment',
            'content_type',
            'object_id',
        ]

    def create(self, validated_data):
        # Retrieve content_type based on the name provided in the request
        content_type_name = validated_data.pop('content_type')

        try:
            content_type = ContentType.objects.get(
                model=content_type_name.lower(),
            )

        except ContentType.DoesNotExist:
            raise serializers.ValidationError(
                {"content_type": "Invalid content type provided."},
            )

        # Assign content_type and object_id to the comment instance
        validated_data['content_type'] = content_type
        return super().create(validated_data)


class CommentReplyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'creator',
            'created_at',
        ]


class CommentListSerializer(serializers.ModelSerializer):
    replies = CommentReplyDetailSerializer(
        many=True,
        read_only=True,
    )
    creator = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'creator',
            'created_at',
            'replies',
        ]
