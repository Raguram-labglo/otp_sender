from rest_framework import serializers
from .models import user_mobile, User
from .helper import *
import random



class Otp_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_mobile
        fields = '__all__'
        read_only_fields = ['isVerified', 'counter', 'user', 'recived_otp']

class Register(serializers.ModelSerializer):
    mobile_no = Otp_serializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'mobile_no']

    def create(self, validated_data):
            data = validated_data.pop('mobile_no')
            user = User.objects.create_superuser(
            username=validated_data['username'],
            email=validated_data['email'],  
            )

            user.set_password(validated_data['password'])
            user.save()

            obj = MessageHandler(str(dict(data)['Mobile']), random.randint(1000, 9999))
            obj.send_otp_via_message()
            return user
