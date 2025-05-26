from django.urls import path

from common.views import (

    HomeView,
    ContactView,
    BlogView,
    PagesView,
    ShopView,
    ShopDetailView,
    ShopingCartView,
    BlogDetailView,
    CheckOutView,
)
from core import settings

app_name = "common"

urlpatterns = [
    path("index/", HomeView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("pages/", PagesView.as_view(), name="pages"),
    path("shop/", ShopView.as_view(), name="shop"),
    path("shop_detail/", ShopDetailView.as_view(), name="shop_detail"),
    path("shopping_cart/", ShopingCartView.as_view(), name="shopping_cart"),
    path("blog_detail/", BlogDetailView.as_view(), name="blog_detail"),
    path("checkout/", CheckOutView.as_view(), name="checkout"),
]
