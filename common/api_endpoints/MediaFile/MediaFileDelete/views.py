from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from common.api_endpoints.MediaFile.MediaFileDelete.serializers import MediaFileDeleteSerializer
from common.models import MediaFile


class MediaFileDeleteAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileDeleteSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'
