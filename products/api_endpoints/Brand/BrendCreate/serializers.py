from rest_framework import serializers

from products.models import Brand

class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
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
    