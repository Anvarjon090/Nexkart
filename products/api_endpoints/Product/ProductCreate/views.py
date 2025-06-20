from rest_framework.generics import CreateAPIView

from products.api_endpoints.Product.ProductCreate.serializers import ProductCreateSerializer
from products.models import Product

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    