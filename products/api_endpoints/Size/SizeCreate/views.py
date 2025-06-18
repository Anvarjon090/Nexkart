from rest_framework.generics import CreateAPIView

from products.api_endpoints.Size.SizeCreate.serializers import SizeCreateSerializer
from products.models import Size

class SizeCreateAPIView(CreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeCreateSerializer
    
    