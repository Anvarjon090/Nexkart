from rest_framework import serializers

from products.models import Color

class ColorDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id']
