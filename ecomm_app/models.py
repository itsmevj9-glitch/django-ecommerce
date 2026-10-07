from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="products/")
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
