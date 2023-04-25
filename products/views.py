from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import product , Productimages,Brand,Category
from django.db.models import Count
# Create your views here.
class productlist(ListView):
    model = product
    paginate_by =50
class productdetail(DetailView):
    model = product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context["images"] = Productimages.objects.filter(product=myproduct)
        '''context['related']=product.objects.filter(category=myproduct)'''
        return context
    
class Brandslist(ListView):
    model = Brand 
    #paginate_by=5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] =Brand.objects.all().annotate(product_count=Count('product_brand'))
        return context
class BrandDetail(DetailView):
    model = Brand
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mybrand = self.get_object()
        context["brand_products"] = product.objects.filter(brand=mybrand)
        return context
    
class categorylist(ListView):
    model = Category 
    #paginate_by=5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] =Category.objects.all().annotate(product_count=Count('product_catrgory'))
        return context
    
    
       
