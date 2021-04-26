from django.shortcuts import render
from django.views import generic

from .models import Product
from category.models import Category

# Create your views here.

class ProductList(generic.ListView):
    model = Product