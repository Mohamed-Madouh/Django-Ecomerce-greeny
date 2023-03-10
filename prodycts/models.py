from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
PRODUCT_FLAG={
    ('New','New' )
    ('Feature', 'Feature' )
    ('sela', 'sela' )
}
class product(models.Model):
    name = models.CharField(_('name'),max_length=100 , )
    sku = models.models.IntegerField(_('sku'))
    subtitle = models.CharField(_('subtitle'),max_length=300)
    desc = models.TextField(_('Description'), max_length=10000)
    flag = models.CharField(_('flag'),max_length=10 , choices=PRODUCT_FLAG)
    price = models.FloatField(_('price'))
    tag =""
    Category=models.ForeignKey('Category',verbose_name=_('Category'),related_name='product_catrgory',on_delete=models.SET_NULL, null=True,blank=True)
    video_url = models.URLField (null=True,blank=True)  
    brand=models.ForeignKey('brand',verbose_name=_('brand'),related_name='product_brand',on_delete=models.SET_NULL, null=True,blank=True)
class Category(models.Model):
    name = models.CharField(_('name'),max_length=100 , )
    image = models.ImageField(_('image'),upload_to='Category')
class Brand(models.Model):
    name = models.CharField(_('name'),max_length=100)
    image = models.ImageField(_('image'),upload_to='brand')
    class ProdactImage(models.Model):
     image = models.ImageField(_('image'),upload_to='ProdactImage')
     product = models.ForeignKey(product,verbose_name=_('product'),related_name='Prodact_image', on_delete=models.CASCADE)
    class ProdactReview(models.Model):
        pass