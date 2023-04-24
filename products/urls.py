from django.urls import path
from .views import productlist ,productdetail ,Brandslist,BrandDetail,categorylist


app_name ='products'
 
urlpatterns = [
     path('', productlist.as_view(), name = 'product_list'),
     path('<int:pk>', productdetail.as_view(), name = 'product_detail'),
     path('brands/', Brandslist.as_view(), name = 'brand_list'),
     path('category/', categorylist.as_view(), name = 'category_list'),
     path('brands/<int:pk>', BrandDetail.as_view(), name = 'brand_detail'),
 ]
 