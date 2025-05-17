from rest_framework.generics import CreateAPIView

from products.api_endpoints.Category.CategoryDelete.serializers import CategoryDeleteSerializer
from products.models import Product


class ProductDeleteAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CategoryDeleteSerializer
    lookup_field = 'id'
