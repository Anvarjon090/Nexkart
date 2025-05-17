from rest_framework.generics import CreateAPIView


from products.api_endpoints.Category.CategoryCreate.serializers import CategoryCreateSerializer
from products.models import Color


class ColorCreateAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = []