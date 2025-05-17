from rest_framework.generics import DestroyAPIView

from products.api_endpoints.Category.CategoryDelete.serializers import CategoryDeleteSerializer
from products.models import Color


class ColorDeleteAPIView(DestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = CategoryDeleteSerializer
    lookup_field = 'id'
