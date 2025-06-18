from rest_framework.generics import DestroyAPIView

from products.api_endpoints.Size.SizeDelete.serializers import SizeDeleteSerializer
from products.models import Size

class SizeDeleteAPIView(DestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeDeleteSerializer
    
    def perform_destroy(self, instance):
        # Custom logic before deleting the instance
        super().perform_destroy(instance)