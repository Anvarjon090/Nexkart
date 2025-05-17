from rest_framework.generics import ListAPIView

from products.models import Color

from products.api_endpoints.Category.CategoryList.serializers import CategoryListSerializer

class ColorListAPIView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []