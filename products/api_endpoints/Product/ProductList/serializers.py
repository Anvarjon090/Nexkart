from rest_framework import serializers

from products.models import Product, Brand, Category


class CategorySerializerForProductList(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class BrandSerializerForProductList(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo']


class ProductListSerializer(serializers.ModelSerializer):
    brand = BrandSerializerForProductList()
    category = CategorySerializerForProductList()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'brand', 'slug', 'category']


