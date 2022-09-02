from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model): 
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=50)
    cat_image = models.ImageField(upload_to='photos/categories',blank=True)
    
    def __str__(self):
        return self.category_name
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
class Product(models.Model):
    product_name    = models.CharField(max_length=50, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(blank=True)
    price           = models.IntegerField()
    image           = models.ImageField(upload_to='photos/product')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.slug, self.category.slug])
    
    def __str__(self):
        return self.product_name
    
    
    