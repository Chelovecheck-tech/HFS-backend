from rest_framework import serializers
from .models import Category, SubCategory, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'category']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()
    brand = serializers.CharField(source='subcategory.category.name', default=None, read_only=True)
    inStock = serializers.SerializerMethodField()
    title = serializers.CharField(source='name')

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'category',
            'subcategory',
            'price',
            'image',
            'description',
            'brand',
            'inStock',
        ]

    def get_category(self, obj):
        return obj.subcategory.category.slug if obj.subcategory and obj.subcategory.category else None

    def get_subcategory(self, obj):
        return obj.subcategory.slug if obj.subcategory else None

    def get_inStock(self, obj):
        return True # Можно доработать под логику наличия
