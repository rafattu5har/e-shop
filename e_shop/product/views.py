from django.shortcuts import render
from django.views import generic

from .models import Product
from category.models import Category

# Create your views here.

class ProductList(generic.ListView):
    model = Product
    template_name = 'product/product_list.html'


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(pk=self.kwargs.get('pk'))