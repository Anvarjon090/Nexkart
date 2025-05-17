from rest_framework import serializers

from products.models import Product

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "slug",
        ]
    def to_representation(self, instance):
        instance = {
            "id": instance.id,
            "name": instance.name,
            "slug": instance.slug,
        }

        return instance
    