from django.urls import path
from .views import productlist ,productdetail
 
 
urlpatterns = [
     path('', productlist.as_view(), name = 'product_list'),
     path('<int:pk>', productdetail.as_view(), name = 'product_detail')
 ]
 