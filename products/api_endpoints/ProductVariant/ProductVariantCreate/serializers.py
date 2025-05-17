from rest_framework import serializers

from products.models import ProductVariant

class ProductVariantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
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
    