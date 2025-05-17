from django.urls import path

from products.api_endpoints.Color import *

urlpatterns = [
    path('read/', ColorListAPIView.as_view(), name="color-list"),
    path('read/<int:id>/', ColoretrieveAPIView.as_view(), name="color-retrieve"),
    path('create/', ColorCreateAPIView.as_view(), name="color-create"),
    path('delete/<int:id>/', ColorDeleteAPIView.as_view(), name="color-delete"),
    path('update/<int:id>/', ColorUpdateAPIView.as_view(), name="color-update"),
]