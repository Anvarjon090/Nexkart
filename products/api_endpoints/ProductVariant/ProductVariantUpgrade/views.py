from rest_framework.generics import UpdateAPIView

from products.api_endpoints.ProductVariant.ProductVariantUpgrade.serializers import ProductVariantUpdateSerializer
from products.models import ProductVariant

class ProductVariantUpdateAPIView(UpdateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantUpdateSerializer
    lookup_field = 'id'
    