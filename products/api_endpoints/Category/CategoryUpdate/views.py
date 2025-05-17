from rest_framework.generics import UpdateAPIView

from products.api_endpoints.Category.CategoryUpdate.serializers import CategoryUpdateSerializer
from products.models import Category

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    lookup_field = 'id'