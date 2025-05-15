from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.api_endpoints.ProductList.serializers import ProductListSerializer


class ProductListAPIView1(APIView):
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        return queryset
    

class ProductListAPIView2(GenericAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    # def get_queryset(self):
    #     queryset = Product.objects.filter(is_active=True)
    #     return queryset


class ProductListAPIView3(ListCreateAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer