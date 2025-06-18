from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import CreateAPIView

from products.api_endpoints.Brand.BrandCreate.serializers import BrandCreateSerializer
from products.models import Brand

class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer
    parser_classes = (MultiPartParser, FormParser) 