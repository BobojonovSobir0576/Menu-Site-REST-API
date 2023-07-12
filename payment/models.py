from django.db import models
from account.models import Restaurant
import uuid


class OrderRestaurant(models.Model):
    unique_id = models.UUIDField('ID',default=uuid.uuid4, editable=False, unique=True)
    token = models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=150)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE,blank=True,null=True)
    create_at = models.DateField(auto_now=False,auto_now_add=True)
    
    def __str__(self):
        return f'{self.restaurant.name}'