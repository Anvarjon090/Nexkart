from rest_framework import serializers

from products.models import ProductVariant


class ProductVariantsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = [
            "id",
            "name",
            "slug",
        ]