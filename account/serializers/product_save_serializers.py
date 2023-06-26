from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.exceptions import AuthenticationFailed

from account.serializers.res_serializers import *
from account.models import *

import json





class ProductSaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = SaveProduct
        fields = ['full_name','phone','detailed_data','files','restaurant']
    
    
class ProductListSerializers(serializers.ModelSerializer):
    restaurant = RestaurantSerializers(read_only=True)
    class Meta:
        model = SaveProduct
        fields = ['id','full_name','phone','detailed_data','files','restaurant']