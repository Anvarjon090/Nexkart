from rest_framework.generics import UpdateAPIView

from products.api_endpoints.Color.ColorUpdate.serializers import ColorUpdateSerializer
from products.models import Color

class ColorUpdateAPIView(UpdateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorUpdateSerializer
    lookup_field = ['id']
    