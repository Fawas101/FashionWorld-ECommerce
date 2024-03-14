from django.contrib import admin
from . models import Category,Product,Variation

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "price",
        "stock",
        "category",
        "modified_date",
        "is_available",
    )
    prepopulated_fields = {"slug": ("product_name",)}

class VariationAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "variation_category",
        "variation_value",
        "is_active",
)
    list_aditable = ('is_active',)
    list_filter = (
        "product",
        "variation_category",
        "variation_value",)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Variation,VariationAdmin)