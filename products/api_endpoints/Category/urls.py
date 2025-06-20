from django.urls import path

from products.api_endpoints.Category import *

urlpatterns = [
    path('read/', CategoryListAPIView.as_view(), name="category-list"),
    path('read/<int:pk>/', CategoryRetrieveAPIView.as_view(), name="category-retrieve"),
    path('create/', CategoryCreateAPIView.as_view(), name="category-create"),
    path('delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name="category-delete"),
    path('update/<int:pk>/', CategoryUpdateAPIView.as_view(), name="category-update"),
]
