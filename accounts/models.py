from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from utils.generate_code import grnerate_code
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile (models.Model):
    user=models.OneToOneField(User , related_name='user_profile' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/')
    code = models.CharField(max_length=10 , default=grnerate_code)
    code_used = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)


@receiver(post_save,sender=User)
def create_profile ( sender , instance ,created , **kwargs ):
    if created:
        Profile.objects.create(user= instance)
        
DATE_TYPE = {
    ('Home','Home'),
    ('Office', 'Office' ),
    ('Academy', 'Academy' ),
    ('Other', 'Other' )
}
class UserPhoneNumber(models.Model):
    user=models.ForeignKey(User,related_name='user_phonr', on_delete= models.CASCADE )
    number=models.CharField(max_length=11)
    type = models.CharField(choices=DATE_TYPE , max_length=10)
    
class UserAddress(models.Model):
    user = models.ForeignKey(User, related_name='user_address', on_delete=models.CASCADE)
    type = models.CharField(choices=DATE_TYPE , max_length=10)
    coountry =CountryField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    region  = models.CharField(max_length=30)
    street = models.CharField(max_length=80)
    notes =  models.CharField(max_length=200)




        