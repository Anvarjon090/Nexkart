from rest_framework.generics import ListAPIView

from products.models import Category

from products.api_endpoints.Category.CategoryList.serializers import CategoryListSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []