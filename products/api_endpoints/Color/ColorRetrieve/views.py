from rest_framework.generics import RetrieveAPIView

from products.api_endpoints.Color.ColorRetrieve.serializers import ColorRetrieveSerializer
from products.models import Color

class ColorRetrieveAPIView(RetrieveAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorRetrieveSerializer
    lookup_field = 'id'
    permission_classes = []
