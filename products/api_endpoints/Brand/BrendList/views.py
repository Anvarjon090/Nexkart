from rest_framework.generics import ListAPIView

from products.models import Brand

from products.api_endpoints.Category.CategoryList.serializers import CategoryListSerializer

class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []