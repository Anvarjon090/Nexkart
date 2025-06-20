from django.urls import path

from products.api_endpoints.Brand import *

urlpatterns = [
    path('create/', BrandCreateAPIView.as_view(), name='brand-create'),
    path('delete/<int:id>/', BrandDeleteAPIView.as_view(), name='brand-delete'),
    path('read/', BrandListAPIView.as_view(), name='brand-list'),
    path('read/<int:id>/', BrandRetrieveAPIView.as_view(), name='brand-retrieve'),
    path('update/<int:id>/', BrandUpdateAPIView.as_view(), name='brand-update'),
]
