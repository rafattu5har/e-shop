from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_image', blank=True)
    pro_description = models.TextField(null=True)
    quatity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    product_cat = models.ForeignKey(Category, related_name='product', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:single', kwargs={'pk':self.pk})
