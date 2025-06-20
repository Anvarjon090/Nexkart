from rest_framework.generics import CreateAPIView
from products.api_endpoints.Category.CategoryCreate.serializers import CategoryCreateSerializer
from products.models import Category

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    
