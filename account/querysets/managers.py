from django.db import models
from datetime import date, timedelta
import datetime as dt
import calendar


from account.models import *


# Restaurant
class RestaurantQuerySet(models.QuerySet):
    
    def check_is_payment(self,user):
        last_date_of_month = calendar.monthrange(date.today().year, date.today().month)[1]
        get_restaurant = self.prefetch_related('author').filter(author = user).first()
        created_at = get_restaurant.create_at 
        add_one_month = created_at + timedelta(days=last_date_of_month)
        interval_of_two_dates = add_one_month - date.today()
        
        if int(interval_of_two_dates.days) <= 0 :
            return False
        else:
            return True
        

class RestaurantManager(models.Manager):
    
    def get_queryset(self):
        return RestaurantQuerySet(self.model, using=self._db)
    
    def check_is_payment(self,user):
        return self.get_queryset().check_is_payment(user)
    
    
    
# Save Product
class SaveProductQuerySet(models.QuerySet):
    def get_product_with_author(self,user):
        return self.prefetch_related('restaurant').filter(restaurant__author = user)

    def get_by_id(self,id):
        return self.filter(id=id)
    
class SaveProductManager(models.Manager):
    
    def get_queryset(self):
        return SaveProductQuerySet(self.model, using=self._db)
    
    def get_product_with_author(self,user):
        return self.get_queryset().get_product_with_author(user)
    
    def get_by_id(self,id):
        return self.get_queryset().get_by_id(id)