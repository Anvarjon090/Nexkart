from rest_framework.generics import ListAPIView

from products.api_endpoints.Brand.BrandList.serializers import BrandListSerializer
from products.models import Brand

class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = []