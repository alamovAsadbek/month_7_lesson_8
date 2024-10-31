from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['phone_number', 'password']

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')
        user = authenticate(phone_number=phone_number, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        if not user.is_active:
            raise serializers.ValidationError("User is not active")
        return {"user": user}


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
