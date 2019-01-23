from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(SubCategory)


def make_product_special(modeladmin, request, queryset):
    queryset.update(special=True)


make_product_special.short_description = 'Онцгой бүтээгдэхүүн болгох'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'thumbnail', 'special']
    actions = [make_product_special]


admin.site.register(ProductImage)
admin.site.register(Slide)
