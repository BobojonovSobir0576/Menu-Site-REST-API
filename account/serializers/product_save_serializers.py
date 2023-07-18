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


class ProductSave(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=10,required=False)
    class Meta:
        model = SaveOrder
        fields = ('id','full_name','phone','detailed_data','comment','files','restaurant')
        
    
    
class ProductSaveListSerializers(serializers.ModelSerializer):
    restaurant = RestaurantSerializers(read_only=True)
    class Meta:
        model = SaveOrder
        fields = ['id','full_name','phone','detailed_data','comment','files','restaurant']