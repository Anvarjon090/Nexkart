from django.urls import path

from products.api_endpoints.Size import *

urlpatterns = [
    path('create/', SizeCreateAPIView.as_view(), name='size-create'),
    path('delete/<int:id>/', SizeDeleteAPIView.as_view(), name='size-delete'),
    path('read/', SizeListAPIView.as_view(), name='size-list'),
    path('read/<int:id>/', SizeRetrieveAPIView.as_view(), name='size-retrieve'),
    path('update/<int:id>/', SizeUpdateAPIView.as_view(), name='size-update'),
]
