from django.urls import path

from products.api_endpoints.Product import *



urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('delete/<int:id>/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('read/', ProductListAPIView.as_view(), name='product-list'),
    path('read/<int:id>/', ProductRetrieveAPIView.as_view(), name='product-retrieve'),
    path('update/<int:id>/', ProductUpdateAPIView.as_view(), name='product-update'),

]
