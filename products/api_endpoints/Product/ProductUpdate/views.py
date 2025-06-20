from rest_framework.generics import UpdateAPIView

from products.api_endpoints.Product.ProductUpdate.serializers import ProductUpdateSerializer
from products.models import Product

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    lookup_field = 'id'
