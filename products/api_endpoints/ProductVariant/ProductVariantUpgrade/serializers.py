from rest_framework import serializers

from products.models import ProductVariant

class ProductVariantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'price', 'product', 'images', 'stock', 'color', 'size']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def validate(self, attrs):
        brand = self.instance

        if 'slug' in attrs:
            slug = attrs['slug']
            if ProductVariant.objects.filter(slug=slug).exclude(id=brand.id).exists():
                raise serializers.ValidationError("Slug must be unique.")
        return attrs
