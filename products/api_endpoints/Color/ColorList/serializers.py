from rest_framework import serializers

from products.models import Color

class ColorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'slug']