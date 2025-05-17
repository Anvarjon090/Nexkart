from rest_framework.generics import DestroyAPIView

from products.api_endpoints.Category.CategoryDelete.serializers import CategoryDeleteSerializer
from products.models import ProductVariant


class ProductVariantDeleteAPIView(DestroyAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = CategoryDeleteSerializer
    lookup_field = 'id'
