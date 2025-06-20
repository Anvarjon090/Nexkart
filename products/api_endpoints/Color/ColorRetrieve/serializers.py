from rest_framework import serializers

from products.models import Color

class ColorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']