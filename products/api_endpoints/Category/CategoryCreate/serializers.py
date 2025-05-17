from rest_framework import serializers

from products.models import Category

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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
    