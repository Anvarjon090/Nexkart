from rest_framework.serializers import ModelSerializer

from products.models import Review


class ReviewCreateSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "product",
            "rating",
            "review",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return super().create(validated_data)