from rest_framework import serializers
from .models import user_mobile, User
from .helper import *
import random
from django.contrib.auth import login,authenticate
from datetime import datetime, timedelta
import time 


class Otp_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_mobile
        fields = ['isVerified', 'user', 'Mobile']
        read_only_fields = ['isVerified', 'user']

class Register(serializers.ModelSerializer):
    mobile_no = Otp_serializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'mobile_no']

    def create(self, validated_data):
        data = validated_data.pop('mobile_no')
        otp_code = random.randint(1000, 9999)
        obj = MessageHandler(str(dict(data)['Mobile']), otp_code)
        obj.send_otp_via_message()
        user = User.objects.create_superuser(
        username=validated_data['username'],
        email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        delta = timedelta(minutes = 3)
        start = datetime.now()
        user_mobile.objects.create(
        user = user, 
        Mobile = dict(data)['Mobile'], 
        counter = otp_code, 
        otp_send_time = start.time(), 
        otp_exp_time = (start+delta).time()
        )
        
        return user

class Otp_verifier(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 500)
    class Meta:
        model = user_mobile
        fields = ['username', 'recived_otp']

class Wether_for_city(serializers.Serializer):
    city = serializers.CharField(max_length = 85)

    