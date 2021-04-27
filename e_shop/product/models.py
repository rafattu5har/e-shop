from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return 'product_image/' + str(instance.created_at) + '.' + extension
  
class Product(models.Model):
    name = models.CharField(max_length=255)
    pro_description = models.TextField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_location, blank=True)
    product_cat = models.ForeignKey(Category, related_name='product', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:single', kwargs={'pk':self.pk})

