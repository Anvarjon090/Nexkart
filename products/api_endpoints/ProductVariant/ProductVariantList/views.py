from rest_framework.generics import ListAPIView

from products.models import ProductVariant

from products.api_endpoints.Category.CategoryList.serializers import CategoryListSerializer

class ProductVariantListAPIView(ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []