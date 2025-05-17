from rest_framework.generics import ListAPIView

from products.api_endpoints.Category.CategoryRetrieve.serializers import CategoryRetrieveSerializer
from products.models import Color

class ColoretrieveAPIView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = CategoryRetrieveSerializer   
    permission_classes = []