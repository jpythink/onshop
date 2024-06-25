from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_image = models.ImageField(upload_to="uploads/%y/%m/%d")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = "categories"

STATUS_CHOICE = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=40, unique=True)
    product_image = models.ImageField(upload_to="uploads/%y/%m/%d")
    color = models.CharField(max_length=40)
    price = models.FloatField(blank = True)
    description = models.TextField(max_length=1000)
    size_S = models.BooleanField(default=False)
    size_M = models.BooleanField(default=False)
    size_L = models.BooleanField(default=False)

    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
