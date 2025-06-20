from rest_framework import serializers

from products.models import Category


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
        ]
    def validate(self, attrs):
        try:
            category = Category.objects.get(id=attrs['id'])
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this ID does not exist.")
        
        return attrs