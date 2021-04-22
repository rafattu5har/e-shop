from django.shortcuts import render
from django.views import generic

from .models import Category
# Create your views here.
class CatList(generic.ListView):
    model = Category
    template_name = 'category/category_list.html'
    
