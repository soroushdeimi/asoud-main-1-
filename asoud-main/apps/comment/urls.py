# urls.py
from django.urls import path
from apps.comment.views import (
    CommentView, 
    CommentDetailView,
    ContentCommentsView
)

urlpatterns = [
    path('create/', CommentView.as_view()),
    path('<int:pk>/', CommentDetailView.as_view()),
    path('comments/<str:content_type>/<str:object_id>/', ContentCommentsView.as_view()),
]