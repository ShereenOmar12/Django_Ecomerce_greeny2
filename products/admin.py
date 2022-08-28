from django.contrib import admin

# Register your models here.
from .models import Product, ProductImages,productReview,Catergory,Brand


class ProductImagesInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','flag']
    inlines = [ProductImagesInline]



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(productReview)
admin.site.register(Catergory)
admin.site.register(Brand)