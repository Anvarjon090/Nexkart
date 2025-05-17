from rest_framework import serializers

from products.models import Color

class ColorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
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
    