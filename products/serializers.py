from rest_framework import serializers
from .models import Product, Category, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    # include related subcategories for frontend convenience
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'subcategories']


class ProductSerializer(serializers.ModelSerializer):
    # Represent category and subcategory by slug (read only); allow writes by slug too
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all(), allow_null=True, required=False)
    subcategory = serializers.SlugRelatedField(slug_field='slug', queryset=Subcategory.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'brand', 'price', 'category', 'subcategory', 'image', 'in_stock', 'created_at']
