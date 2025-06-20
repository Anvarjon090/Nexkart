from django.urls import path

from accounts.api_endpoints.CartItem import (
    CartItemCreateAPIView,
    CartItemDeleteAPIView,
    CartItemListAPIView,
    # CartItemRetrieveAPIView,
    CartItemUpdateAPIView,

)

urlpatterns = [
    path('create/', CartItemCreateAPIView.as_view(), name='cart-item-create'),
    path('delete/<int:id>/', CartItemDeleteAPIView.as_view(), name='cart-item-delete'),
    path("read/", CartItemListAPIView.as_view(), name="cart-item-list"),
    # path('read/<int:id>/', CartItemRetrieveAPIView.as_view(), name='cart-item-retrieve'),
    path('update/<int:id>/', CartItemUpdateAPIView.as_view(), name='cart-item-update'),

]
