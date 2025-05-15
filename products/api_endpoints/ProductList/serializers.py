from rest_framework import serializers

from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "brand",
        ]
    
    def to_representation(self, instance):
        instance = {
            "id": instance.id,
            "name": instance.name,
            "description": instance.description,
            "brand": instance.brand.name,
            "slug": instance.slug,
            "is_active": instance.is_active,
            "category": instance.category.id if instance.category else None
        }

        return instance