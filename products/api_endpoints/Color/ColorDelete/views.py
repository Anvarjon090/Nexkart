from rest_framework.generics import CreateAPIView

from products.api_endpoints.Category.CategoryDelete.serializers import CategoryDeleteSerializer
from products.models import Color


class ColorDeleteAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = CategoryDeleteSerializer
    lookup_field = 'id'
