from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from products.models import Review, Comment
from products.api_endpoints.ReviewComment.ReviewCommentCreate.serializers import (
    ReviewCreateSerializer
)


class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)