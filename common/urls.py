from django.urls import path

from common.views import *
from common.api_endpoints import *

app_name = "common"

urlpatterns = [
    path("media/upload/", MediaFileCreateAPIView.as_view(), name="media-upload"),
    path("media/delete/<int:id>/", MediaFileDestroyAPIView.as_view(), name="media-delete"),

    # templates
    path("", HomeView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog/details/", BlogDetailView.as_view(), name="blog-details"),
    path("cart/", ShoppingCartView.as_view(), name="shopping-cart"),
    path("profile/", ProfileView.as_view(), name="profile"),
]