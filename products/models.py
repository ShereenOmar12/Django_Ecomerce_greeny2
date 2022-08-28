from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

PRODUCT_FLAG =(
('New','New'),
('Feature','Feature'),
('Sale','Sale')                                                                       
)

class Product(models.Model):
    name=models.CharField(_('Name'),max_length=100)
    sku =models.IntegerField(_('SKU'))
    subtitle= models.CharField(_('Subtitle'),max_length=300)
    desc= models.TextField(_('Description'),max_length=10000)
    flag=models.CharField(_('Flag'),max_length=10,choices=PRODUCT_FLAG)
    price =models.FloatField(_('Price'))
    tags=TaggableManager()
    category=models.ForeignKey('Catergory',verbose_name=_('Category'),related_name='product_catrgory',on_delete=models.SET_NULL,null=True,blank=True)
    brand=models.ForeignKey('Brand',verbose_name=_('Brand'),related_name='product_review',on_delete=models.SET_NULL,null=True,blank=True)
    video_url=models.URLField(null=True,blank=True)
    
    def __str__(self):
        return str(self.name)

class ProductImages(models.Model):
    product=models.ForeignKey(Product,verbose_name=_('Product'),related_name='product_category',on_delete=models.SET_NULL,null=True,blank=True) 
    image= models.ImageField(verbose_name=_('Image'),upload_to='productimages')

    def __str__(self):
        return str(self.product)


class Catergory(models.Model):
    name=models.CharField(_('Name'),max_length=100)
    image=models.ImageField(_('Image'),upload_to='category')
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    name=models.CharField(_('Name'),max_length=100)
    image=models.ImageField(_('Image'),upload_to='Brand')

    def __str__(self):
        return self.name

class productReview(models.Model):
    usr=models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    product= models.ForeignKey(Product,verbose_name=_('Product'),related_name='product_review',on_delete=models.SET_NULL,null=True,blank=True)
    rate=models.IntegerField(verbose_name=_('Rate'))
    review=models.CharField(verbose_name=_('Name'),max_length=300)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
         return str(self.product)
