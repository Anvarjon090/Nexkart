from rest_framework.generics import UpdateAPIView

from products.api_endpoints.Size.SizeUpdate.serializers import SizeUpdateSerializer
from products.models import Size

class SizeUpdateAPIView(UpdateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeUpdateSerializer
    lookup_field = 'id'
    