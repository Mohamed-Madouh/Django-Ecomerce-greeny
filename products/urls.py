from django.urls import path
from .views import productlist
 
 
urlpatterns = [
     path('', productlist.as_view(), name = 'product_list')
 ]
 