from django.contrib import admin

# Register your models here.
from .models import Product, ProductImages,productReview,Catergory,Brand
from django_summernote.admin import SummernoteModelAdmin



class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name','price','flag']
    inlines = [ProductImagesInline]


    



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(productReview)
admin.site.register(Catergory)
admin.site.register(Brand)