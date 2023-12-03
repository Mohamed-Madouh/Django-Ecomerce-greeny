from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import product
from django.shortcuts import render

@api_view(['GET'])
def product_list_api(request):
    objects = product.objects.all()
    data = ProductSerializer(objects, many = True).data
    return Response({'status':200 ,'all products':data})
@api_view(['GET'])
def Detailprodctapi(request,id):
    objects = product.objects.get(id=id)
    data = ProductSerializer(objects).data
    return Response({'status':200 ,'all products':data})
# class productlistapi(generics.ListAPIView):
#     querysrt=product.objects.all()
#     serializer_class =ProductSerializer
class ProductListAPI(generics.ListCreateAPIView):
    queryset=product.objects.all()
    serializer_class =ProductSerializer
class ProducDetailtAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset=product.objects.all()
    serializer_class =ProductSerializer
    
