from django.shortcuts import render
from django.views.generic import ListView
from .models import product
# Create your views here.
class productlist(ListView):
    model = product
