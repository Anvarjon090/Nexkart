from rest_framework import serializers

from products.models import Product

class ProductDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'slug', 'default_imaes', 'category']
        