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
