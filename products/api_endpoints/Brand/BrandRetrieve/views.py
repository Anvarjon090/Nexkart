from rest_framework.generics import RetrieveAPIView

from products.api_endpoints.Brand.BrandRetrieve.serializers import BrandRetrieveSerializer
from products.models import Brand

class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandRetrieveSerializer
    lookup_field = 'id'
    permission_classes = []
    