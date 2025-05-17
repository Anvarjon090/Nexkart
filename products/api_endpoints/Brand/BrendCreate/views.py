from rest_framework.generics import CreateAPIView


from products.api_endpoints.Category.CategoryCreate.serializers import CategoryCreateSerializer
from products.models import Brand


class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = []