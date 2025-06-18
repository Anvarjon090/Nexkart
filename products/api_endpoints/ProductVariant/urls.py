from django.urls import path

from products.api_endpoints.ProductVariant import *

urlpatterns = [
    path('create/', ProductVariantCreateAPIView.as_view(), name='productvariant-create'),
    path('delete/<int:id>/', ProductVariantDeleteAPIView.as_view(), name='productvariant-delete'),
    path('read/', ProductVariantListAPIView.as_view(), name='productvariant-list'),
    path('read/<int:id>/', ProductVariantRetrieveAPIView.as_view(), name='productvariant-retrieve'),
    path('update/<int:id>/', ProductVariantUpdateAPIView.as_view(), name='productvariant-update'),
]
