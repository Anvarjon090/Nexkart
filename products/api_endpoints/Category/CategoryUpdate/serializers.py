from rest_framework import serializers

from products.models import Category

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ['id']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def validate(self, attrs):
        category = self.instance

        if 'slug' in attrs:
            slug = attrs['slug']
            if Category.objects.filter(slug=slug).exclude(id=category.id).exists():
                raise serializers.ValidationError("Slug must be unique.")
        return attrs