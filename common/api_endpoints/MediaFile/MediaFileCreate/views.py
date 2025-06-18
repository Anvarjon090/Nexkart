from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import CreateAPIView

from common.api_endpoints.MediaFile.MediaFileCreate.serializers import MediaFileCreateSerializer
from common.models import MediaFile


class MediaFileCreateAPIView(CreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileCreateSerializer
    parser_classes = (MultiPartParser, FormParser)
    