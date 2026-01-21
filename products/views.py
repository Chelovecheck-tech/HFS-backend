from rest_framework import viewsets
from .models import Product, Category, Subcategory
from .serializers import ProductSerializer, CategorySerializer, SubcategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """API for products. Supports optional filtering by ?category=<slug> and/or ?subcategory=<slug>."""
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all().order_by('-created_at')
        category = self.request.query_params.get('category')
        subcategory = self.request.query_params.get('subcategory')
        if category:
            qs = qs.filter(subcategory__category__slug=category)
        if subcategory:
            qs = qs.filter(subcategory__slug=subcategory)
        return qs


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """List/retrieve categories with nested subcategories."""
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subcategory.objects.all().order_by('name')
    serializer_class = SubcategorySerializer
