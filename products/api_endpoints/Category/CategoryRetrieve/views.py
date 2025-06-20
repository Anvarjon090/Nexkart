from rest_framework.generics import RetrieveAPIView

from products.models import Category
from products.api_endpoints.Category.CategoryRetrieve.serializers import CategoryRetrieveSerializer

class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetrieveSerializer
    permission_classes = []
    
