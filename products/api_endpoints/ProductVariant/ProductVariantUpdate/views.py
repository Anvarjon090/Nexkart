from rest_framework.generics import UpdateAPIView

from products.api_endpoints.Category.CategoryUpdate.serializers import CategoryUpdateSerializer
from products.models import ProductVariant

class ProductVariantUpdateAPIView(UpdateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = CategoryUpdateSerializer
    lookup_field = 'id'