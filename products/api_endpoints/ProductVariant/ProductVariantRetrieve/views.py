from rest_framework.generics import ListAPIView

from products.api_endpoints.Category.CategoryRetrieve.serializers import CategoryRetrieveSerializer
from products.models import ProductVariant

class ProductVariantRetrieveAPIView(ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = CategoryRetrieveSerializer 