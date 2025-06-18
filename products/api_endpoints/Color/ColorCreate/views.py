from rest_framework.generics import CreateAPIView

from products.api_endpoints.Color.ColorCreate.serializers import ColorCreateSerializer
from products.models import Color

class ColorCreateAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorCreateSerializer
    
    