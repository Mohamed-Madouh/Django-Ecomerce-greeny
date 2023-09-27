from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from utils.generate_code import grnerate_code
from products.models import product

# Create your models here.


STATUS_CHOICES={
    ('inprogress','inprogress'),
    ('complated','complated'),

    
}




class Cart(models.Model):
    code = models.CharField(max_length=8 ,default=grnerate_code)
    user = models.ForeignKey(User,related_name='user_cart',on_delete=models.SET_NULL,null=True ,blank= True)

    status= models.CharField(choices=STATUS_CHOICES ,max_length=10)
    
    def __str__(self) :
        return str(self.code)
    
class CartDetail(models.Model):
    cart= models.ForeignKey(Cart ,related_name= 'cart_detatil', on_delete=models.CASCADE)
    product = models.ForeignKey(product , related_name='cart_product', on_delete=models.SET_NULL ,null=True , blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    
    def __str__(self) :
       return str(self.cart)

















STATUS_CHOICES={
    ('receieved','receieved'),
    ('processed','processed'),
    ('shiped','shiped'),
    ('delivered','delivered'),
    
}




class Order(models.Model):
    code = models.CharField(max_length=8 ,default=grnerate_code)
    user = models.ForeignKey(User,related_name='userorder',on_delete=models.SET_NULL,null=True ,blank= True)
    order_time =models.DateField(default=timezone.now)
    delivery_time =models.DateField(null=True,blank=True)
    status= models.CharField(choices=STATUS_CHOICES ,max_length=10)
    
    def __str__(self) :
        return str(self.code)
    
class OrderDetail(models.Model):
    order= models.ForeignKey(Order ,related_name= 'order_detatil', on_delete=models.CASCADE)
    product = models.ForeignKey(product , related_name='order_product', on_delete=models.SET_NULL ,null=True , blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    
    def __str__(self) :
       return str(self.order)
    
    