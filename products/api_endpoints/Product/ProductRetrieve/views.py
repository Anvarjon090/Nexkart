from rest_framework.generics import RetrieveAPIView

from products.api_endpoints.Product.ProductRetrieve.serializers import ProductRetrieveSerializer
from products.models import Product

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer
    permission_classes = []
    lookup_field = 'id'