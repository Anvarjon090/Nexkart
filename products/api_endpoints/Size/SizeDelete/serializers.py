from rest_framework import serializers

from products.models import Size

class SizeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id']
