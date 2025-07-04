from rest_framework.generics import DestroyAPIView

from products.api_endpoints.Category.CategoryDelete.serializers import CategoryDeleteSerializer
from products.models import Product


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CategoryDeleteSerializer
    lookup_field = 'id'
