from django.db import models
from django.contrib.auth.models import *
from account.querysets.managers import *
import uuid


class Restaurant(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    logo = models.ImageField(upload_to = 'logo/')
    price = models.IntegerField(default=0)
    is_payment = models.BooleanField(default=False)
    create_at = models.DateField()
    author = models.ManyToManyField(User)
    
    objects = RestaurantManager()
    
    def __str__(self):
        return self.name
    

class Catalog(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    img = models.ImageField(upload_to = 'catalog/')
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    img = models.ImageField(upload_to = 'product/')
    price = models.IntegerField(default=0)
    gramms = models.FloatField(default=0)
    description = models.TextField()
    catalog = models.ForeignKey(Catalog, on_delete = models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class SaveProduct(models.Model):
    full_name = models.CharField(max_length=150,null=True,blank=True)
    phone = models.CharField(max_length=150,null=True,blank=True)
    detailed_data = models.JSONField(null=True,blank=True)
    files = models.FileField(blank=True,null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    obj = SaveProductManager()
    
    def __str__(self):
        return self.full_name
    
    

class Order(models.Model):
    unique_id = models.UUIDField('ID',default=uuid.uuid4, editable=False, unique=True)
    token = models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=150)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE,blank=True,null=True)