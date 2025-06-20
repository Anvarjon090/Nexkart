from rest_framework.generics import GenericAPIView
from rest_framework import permissions

from accounts.models import CartItem


class CartItemDeleteAPIView(GenericAPIView):
    query_set = CartItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
__all__ = ["CartItemDeleteAPIView"]