from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from utils.genereate_code import generate_code
from products.models import Product






STATUS_CHOICES = (
('inprogress','inprogress'),
('completed','completed'),

)




# Create your models here.

class Cart(models.Model):
    code = models.CharField(max_length=8,default=generate_code)
    user = models.ForeignKey(User, related_name='user_cart',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(choices=STATUS_CHOICES,  max_length=8)

    def __str__(self):
        return self.code





class CartDetail(models.Model):
    cart=models.ForeignKey(Order,related_name=' cart_detail', on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,related_name='cart_product', on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField()
    price=models.FloatField()
    total= models.FloatField()

    def __str__(self):
        return str(self.order)







STATUS_CHOICES = (
('receieved','receieved'),
('processed','processed'),
('shiped','shiped'),
('delivered','delivered'),
)




# Create your models here.

class Order(models.Model):
    code = models.CharField(max_length=8,default=generate_code)
    user = models.ForeignKey(User, related_name='user_order',on_delete=models.SET_NULL,null=True,blank=True)
    order_time= models.DateTimeField(default=timezone.now)
    delivery_time= models.DateTimeField(null=True,blank=True)
    status = models.CharField(choices=STATUS_CHOICES,  max_length=8)

    def __str__(self):
        return self.code





class OrderDetail(models.Model):
    order=models.ForeignKey(Order,related_name='order_detail', on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,related_name='order_product', on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField()
    price=models.FloatField()
    total= models.FloatField()

    def __str__(self):
        return str(self.order)


