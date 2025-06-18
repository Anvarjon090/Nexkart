from rest_framework.generics import CreateAPIView

from products.api_endpoints.ProductVariant.ProductVariantCreate.serializers import ProductVariantCreateSerializer
from products.models import ProductVariant

class ProductVariantCreateAPIView(CreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantCreateSerializer
    