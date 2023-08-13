from django.contrib import admin

from apps.products.models import Product, Category, Tag


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'description',
    ]

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(Tag)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
