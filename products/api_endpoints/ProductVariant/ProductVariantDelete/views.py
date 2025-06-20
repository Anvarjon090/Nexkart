from rest_framework.generics import DestroyAPIView

from products.api_endpoints.ProductVariant.ProductVariantDelete.serializers import ProductVariantDeleteSerializer
from products.models import ProductVariant

class ProductVariantDeleteAPIView(DestroyAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantDeleteSerializer
    lookup_field = 'id'