from rest_framework import serializers

from products.models import Size

class SizeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']