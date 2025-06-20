from rest_framework.generics import ListAPIView

from products.api_endpoints.ProductVariant.ProductVariantList.serializers import ProductVariantListSerializer
from products.models import ProductVariant

class ProductVariantListAPIView(ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantListSerializer
    permission_classes = []