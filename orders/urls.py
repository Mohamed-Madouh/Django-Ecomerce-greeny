from django.urls import path
from .views import add_to_cart


app_name ='orders'
 
urlpatterns = [
     path('add_to_car' , add_to_cart, name= 'add_to_cart'),
     ]
