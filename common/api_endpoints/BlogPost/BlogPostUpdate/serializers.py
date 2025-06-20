from rest_framework import serializers

from products.models import Brand

class BrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo']
        read_only_fields = ['id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def validate(self, attrs):
        brand = self.instance

        if 'slug' in attrs:
            slug = attrs['slug']
            if Brand.objects.filter(slug=slug).exclude(id=brand.id).exists():
                raise serializers.ValidationError("Slug must be unique.")
        return attrs