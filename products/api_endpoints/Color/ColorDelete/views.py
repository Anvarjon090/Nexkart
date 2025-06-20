from rest_framework.generics import DestroyAPIView

from products.api_endpoints.Color.ColorDelete.serializers import ColorDeleteSerializer
from products.models import Color

class ColorDeleteAPIView(DestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorDeleteSerializer
    
    def perform_destroy(self, instance):
        # Custom logic before deleting the instance
        super().perform_destroy(instance)