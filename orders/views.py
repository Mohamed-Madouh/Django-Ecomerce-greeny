from django.shortcuts import render 
from urllib import request
from products.models import product
from .models import Cart ,CartDetail
# Create your views here.
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        
        prodect = product.object.get(id = product_id)
        cart = Cart.object.get(user = request.user , status = 'inprogress')
        cart_detail ,created = CartDetail.objects.get_or_create(
            cart = cart,
            prodect = prodect
        )
        cart_detail.quantity = quantity
        cart_detail.price = product.price
        cart_detail.total = int(quantity)* product.price
        cart_detail.save()
