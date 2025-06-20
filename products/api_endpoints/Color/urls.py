from django.urls import path

from products.api_endpoints.Color import *

urlpatterns = [
    path('create/', ColorCreateAPIView.as_view(), name='color-create'),
    path('delete/<int:id>/', ColorDeleteAPIView.as_view(), name='color-delete'),
    path('read/', ColorListAPIView.as_view(), name='color-list'),
    path('read/<int:id>/', ColorRetrieveAPIView.as_view(), name='color-retrieve'),
    path('update/<int:id>/', ColorUpdateAPIView.as_view(), name='color-update'),
]
