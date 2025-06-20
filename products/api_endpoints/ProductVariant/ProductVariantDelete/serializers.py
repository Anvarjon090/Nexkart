from rest_framework import serializers

from products.models import ProductVariant

class ProductVariantDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'price', 'product', 'images', 'stock', 'color', 'size']
