from django.urls import path

from products.api_endpoints.ReviewComment import (
    ReviewCreateAPIView,
    ReviewDeleteAPIView,
    UserReviewsListAPIView,
    UserCommentsListAPIView
)

urlpatterns = [
    path('create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('delete/<int:pk>/', ReviewDeleteAPIView.as_view(), name='review-delete'),
    path('user-reviews/', UserReviewsListAPIView.as_view(), name='user-reviews-list'),
    path('user-comments/', UserCommentsListAPIView.as_view(), name='user-comments-list'),
]
