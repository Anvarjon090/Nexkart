from rest_framework.generics import ListAPIView

from products.api_endpoints.Color.ColorList.serializers import ColorListSerializer
from products.models import Color

class ColorListAPIView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorListSerializer
    lookup_field = 'id'
    permission_classes = []
    