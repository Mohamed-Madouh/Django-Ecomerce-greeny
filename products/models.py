from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone  #import time zone
from django.contrib.auth.models import User 
from taggit.managers import TaggableManager
from django.db.models.aggregates import Max ,Min,Avg ,Sum
# Create your models here.
PRODUCT_FLAG={
    ('New','New'),
    ('Feature', 'Feature' ),
    ('sela', 'sela' )
}
class product(models.Model):
    name = models.CharField(_('name'),max_length=100 , )
    sku = models.IntegerField(_('sku'))
    subtitle = models.CharField(_('subtitle'),max_length=300)
    desc = models.TextField(_('Description'), max_length=10000)
    flag = models.CharField(_('flag'),max_length=10 , choices=PRODUCT_FLAG)
    price = models.FloatField(_('price'))
    image = models.ImageField(_('image'),upload_to='products')
    tag =TaggableManager()
    category=models.ForeignKey('Category',verbose_name=_('Category'),related_name='product_catrgory',on_delete=models.SET_NULL, null=True,blank=True)
    video_url = models.URLField (null=True,blank=True)  
    brand=models.ForeignKey('Brand',verbose_name=_('brand'),related_name='product_brand',on_delete=models.SET_NULL, null=True,blank=True)
    Quantity= models.IntegerField(default=50)
    def __str__(self) :
       return self.name
    def get_avg(self):
        avg = self.Prodact_review.aggregate(myavg= Avg("rate"))
        return avg
       
class Productimages(models.Model):
    image = models.ImageField(_('image'),upload_to='Productimages')
    product = models.ForeignKey(product,verbose_name=_('product'),related_name='Product_images', on_delete=models.CASCADE)
    def __str__(self) -> str:
       return str(self.product)
class ProdactReviews(models.Model):
    user = models.ForeignKey (User , related_name='user_review', on_delete=models.SET_NULL ,null=True, blank=True)
    product= models.ForeignKey(product, verbose_name=_("product"),related_name='Prodact_review', on_delete=models.SET_NULL,null =True,blank =True)
    rate =models.IntegerField(verbose_name=('rate'))
    review =models.CharField(verbose_name=('review'),max_length=300)
    created_at =models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return str(self.product)
class Category(models.Model):
    name = models.CharField(_('name'),max_length=100 , )
    image = models.ImageField(_('image'),upload_to='Category')
    def __str__(self) :
       return self.name

class Brand(models.Model):
    name = models.CharField(_('name'),max_length=100)
    image = models.ImageField(_('image'),upload_to='Brand')
    def __str__(self) :
       return self.name

