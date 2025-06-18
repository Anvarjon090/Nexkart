from django.urls import path

from common.views import (
    HomeView, 
    ContactView,
    BlogView,
    CheckoutView, 
    ShopGridView, 
    BlogDetailsView, 
    ShopDetailsView, 
    ShopingCartView,
)

app_name = "common"

urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('shop-grid/', ShopGridView.as_view(), name='shop_grid'),
    path('blog-details/', BlogDetailsView.as_view(), name='blog_details'),
    path('shop-details/', ShopDetailsView.as_view(), name='shop_details'),
    path('shopping-cart/', ShopingCartView.as_view(), name='shopping_cart'),
]
