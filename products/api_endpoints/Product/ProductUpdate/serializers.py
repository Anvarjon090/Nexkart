from rest_framework import serializers

from products.models import Product

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'brand', 'slug', 'default_images', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def validate(self, attrs):
        brand = self.instance

        if 'slug' in attrs:
            slug = attrs['slug']
            if Product.objects.filter(slug=slug).exclude(id=brand.id).exists():
                raise serializers.ValidationError("Slug must be unique.")
        return attrs
