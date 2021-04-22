from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    cat_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.cat_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['cat_name']
