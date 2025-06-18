from rest_framework.generics import ListAPIView

from common.api_endpoints.MediaFile.MediaFileList.serializers import MediaFileListSerializer
from common.models import MediaFile

class MediaFileListAPIView(ListAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileListSerializer
    lookup_field = 'id'