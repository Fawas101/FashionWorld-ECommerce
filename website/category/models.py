from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=600, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('products_by_category', args = [self.slug])

    def __str__(self):
        return self.category_name   
    

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="photos/products")
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
         return reverse('product_details', args=[self.category.slug,self.slug])

    def save(self, *args, **kwargs):
        if self.stock < 0:
            self.stock = 0

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name
    
class VariationManager(models.Manager):
     def colors(self):
          return super(VariationManager, self).filter(variation_category = 'color',is_active=True)
     def sizes(self):
          return super(VariationManager, self).filter(variation_category = 'size',is_active=True)

variation_category_choice =(
    ('color', 'color'),
    ('size','size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default = True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __unicode__(self):
         return self.product 