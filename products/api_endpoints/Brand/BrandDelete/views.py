from rest_framework.generics import DestroyAPIView

from products.api_endpoints.Brand.BrandDelete.serializers import BrandDeleteSerializer
from products.models import Brand

class BrandDeleteAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDeleteSerializer

    def perform_destroy(self, instance):
        # Custom logic before deleting the instance
        super().perform_destroy(instance)