from rest_framework import serializers
from .models import product, Category,Brand

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields='__all__'




class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand= serializers.StringRelatedField()
    
    
    # price_with_tax_1 = serializers.SerializerMethodField(method_name='price_with_tax_1')
    class  Meta:
        model = product
        fields ='__all__'
        
        
    # def price_with_tax_1(self,product:product):
    #     return product.price*1.1   
     
