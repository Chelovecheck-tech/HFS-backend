from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, SubcategoryViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'subcategories', SubcategoryViewSet, basename='subcategory')

urlpatterns = [
    # Router provides /products/, /categories/ and /subcategories/ endpoints
    path('', include(router.urls)),
]



