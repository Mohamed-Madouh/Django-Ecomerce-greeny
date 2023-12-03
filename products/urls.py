from django.urls import path
from .views import productlist ,productdetail ,Brandslist,BrandDetail,categorylist
from .api import product_list_api ,ProductListAPI,Detailprodctapi,ProducDetailtAPI
# from rest_framework.decorators import api_view

app_name ='products'
 
urlpatterns = [
     path('', productlist.as_view(), name = 'product_list'),
     path('<int:pk>', productdetail.as_view(), name = 'product_detail'),
     path('brands/', Brandslist.as_view(), name = 'brand_list'),
     path('category/', categorylist.as_view(), name = 'category_list'),
     path('brands/<int:pk>', BrandDetail.as_view(), name = 'brand_detail'),
     path('api/', product_list_api),
     path('api/<int:id>', Detailprodctapi),
     path('api/cbv/<int:pk>', ProducDetailtAPI.as_view()),
     path('api/cbv',ProductListAPI.as_view()),
     
#api   
     
     # path('api/' ,product_list_api),
     
     
 ]
 