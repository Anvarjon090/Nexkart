from rest_framework import serializers

from products.models import Size

class SizeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name', 'slug']