from rest_framework.generics import CreateAPIView

from products.api_endpoints.Category.CategoryDelete.serializers import CategoryDeleteSerializer
from products.models import Brand


class BrandDeleteAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = CategoryDeleteSerializer
    lookup_field = 'id'
