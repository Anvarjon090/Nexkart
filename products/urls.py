from django.urls import path
from products.api_endpoints.ProductList.views import (
    ProductListAPIView1,
    ProductListAPIView2,
    ProductListAPIView3
)

urlpatterns = [
    path('list1/', ProductListAPIView1.as_view(), name="product-list1"),
    path('list2/', ProductListAPIView2.as_view(), name="product-list2"),
    path('list3/', ProductListAPIView3.as_view(), name="product-list3"),
]
