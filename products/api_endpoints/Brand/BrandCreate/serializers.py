from rest_framework import serializers

from products.models import Brand

class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo']
        extra_kwargs = {
            'name': {'required': True},
            'slug': {'required': True},
            'logo': {'required': False}
        }
        read_only_fields = ['id']