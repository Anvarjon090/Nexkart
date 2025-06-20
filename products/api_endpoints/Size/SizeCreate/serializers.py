from rest_framework import serializers

from products.models import Size

class SizeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
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