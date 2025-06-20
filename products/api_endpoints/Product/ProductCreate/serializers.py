from rest_framework import serializers

from products.models import Product

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'slug', 'brand', 'default_images', 'category']
        extra_kwargs = {
            'description': {'required': False},
        }

