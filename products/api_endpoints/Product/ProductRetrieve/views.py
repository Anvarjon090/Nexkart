from rest_framework.generics import ListAPIView

from products.api_endpoints.Category.CategoryRetrieve.serializers import CategoryRetrieveSerializer
from products.models import Product

class ProductRetrieveAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = CategoryRetrieveSerializer   
    permission_classes = []