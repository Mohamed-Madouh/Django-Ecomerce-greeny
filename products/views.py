from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import product , Productimages
# Create your views here.
class productlist(ListView):
    model = product
class productdetail(DetailView):
    model = product
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            myproduct = self.get_object()
            context['related']= product.objects.filter(category = myproduct.category)
            context["imges"] = Productimages.objects.filter(product=myproduct)
            return context
        
