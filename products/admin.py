from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category, Subcategory


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SubcategoryInline]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'price', 'in_stock', 'category', 'subcategory', 'image_preview', 'created_at')
    list_display_links = ('title',)
    search_fields = ('title', 'brand')
    list_filter = ('in_stock', 'category', 'subcategory')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' style='max-height:70px; max-width:120px;'/>")
        return "-"

    image_preview.short_description = 'Фото'
