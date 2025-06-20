from rest_framework import serializers

from products.models import Product, Category, Brand 


class CategorySerializerForProductRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']


class BrandSerializerForProductRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo', 'created_at', 'updated_at']
   

class ProductRetrieveSerializer(serializers.ModelSerializer): 
    brand = BrandSerializerForProductRetrieve()
    category = CategorySerializerForProductRetrieve()
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'brand', 'slug', 'category', 'is_active', 'created_at', 'updated_at']
        