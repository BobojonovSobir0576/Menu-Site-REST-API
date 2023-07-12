from django.contrib import admin
from payment.models import *


@admin.register(OrderRestaurant)
class OrderRestaurantAdmin(admin.ModelAdmin):
    list_display = ('token','restaurant','unique_id')