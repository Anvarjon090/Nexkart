from rest_framework.generics import RetrieveAPIView

from products.api_endpoints.ProductVariant.ProductVariantRetrieve.serializers import ProductVariantRetrieveSerializer
from products.models import ProductVariant

class ProductVariantRetrieveAPIView(RetrieveAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantRetrieveSerializer
    permission_classes = []
    lookup_field = 'id'