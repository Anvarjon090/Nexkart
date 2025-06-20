from rest_framework.generics import ListAPIView

from products.api_endpoints.Size.SizeList.serializers import SizeListSerializer
from products.models import Size

class SizeListAPIView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer
    lookup_field = 'id'
    permission_classes = []
    