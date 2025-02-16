from django.urls import path

from apps.comment.views.user_views import (
    CommentCreateAPIView,
    CommentListAPIView,
)

app_name = 'comment_user'

urlpatterns = [
    path(
        'create/',
        CommentCreateAPIView.as_view(),
        name='create',
    ),
    path(
        'list/',
        CommentListAPIView.as_view(),
        name='list',
    ),
]
