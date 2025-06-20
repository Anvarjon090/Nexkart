from rest_framework import serializers

from products.models import ProductVariant, Product, Color, Size, Category, Brand


class CategorySerializerForProductVariantRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']


class BrandSerializerForProductVariantRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo', 'created_at', 'updated_at']


class ProductSerializerForProductVariantRetrieve(serializers.ModelSerializer):
    brand = BrandSerializerForProductVariantRetrieve()
    category = CategorySerializerForProductVariantRetrieve()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'brand', 'slug', 'category', 'is_active', 'created_at', 'updated_at']


class ColorSerializerForProductVariantRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']


class SizeSerializerForProductVariantRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']






class ProductVariantRetrieveSerializer(serializers.ModelSerializer):
    product = ProductSerializerForProductVariantRetrieve()
    color = ColorSerializerForProductVariantRetrieve()
    size = SizeSerializerForProductVariantRetrieve()

    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'price', 'product', 'images', 'stock', 'color', 'size', 'is_active', 'created_at', 'updated_at']
        
