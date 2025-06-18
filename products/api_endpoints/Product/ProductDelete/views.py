from rest_framework.generics import DestroyAPIView

from products.api_endpoints.Product.ProductDelete.serializers import ProductDeleteSerializer
from products.models import Product

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDeleteSerializer
    lookup_field = 'id'
