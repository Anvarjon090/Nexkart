from rest_framework.generics import RetrieveAPIView

from products.api_endpoints.Size.SizeRetrieve.serializers import SizeRetrieveSerializer
from products.models import Size

class SizeRetrieveAPIView(RetrieveAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeRetrieveSerializer
    lookup_field = 'id'
    permission_classes = []
