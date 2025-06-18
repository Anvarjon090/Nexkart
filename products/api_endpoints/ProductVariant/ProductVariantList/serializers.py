from rest_framework import serializers

from products.models import ProductVariant, Product, Color, Size, Category, Brand


class CategorySerializerForProductVariantList(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class BrandSerializerForProductVariantList(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo']


class ProductSerializerForProductVariantList(serializers.ModelSerializer):
    brand = BrandSerializerForProductVariantList()
    category = CategorySerializerForProductVariantList()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'brand', 'slug', 'category']


class ColorSerializerForProductVariantList(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'slug']


class SizeSerializerForProductVariantList(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name', 'slug']


class ProductVariantListSerializer(serializers.ModelSerializer):
    product = ProductSerializerForProductVariantList()
    color = ColorSerializerForProductVariantList()
    size = SizeSerializerForProductVariantList()

    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'price', 'product', 'images', 'stock', 'color', 'size']
