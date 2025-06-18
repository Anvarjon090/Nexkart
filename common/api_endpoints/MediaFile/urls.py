from django.urls import path

from common.api_endpoints.MediaFile import *

urlpatterns = [
    path('create/', MediaFileCreateAPIView.as_view(), name='mediafile-create'),
    path('delete/<int:id>/', MediaFileDeleteAPIView.as_view(), name='mediafile-delete'),
    path('read/', MediaFileListAPIView.as_view(), name='mediafile-list'),
]
