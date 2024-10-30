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
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        if not user.is_active:
            raise serializers.ValidationError("User is not active")
        return {"user": user}
