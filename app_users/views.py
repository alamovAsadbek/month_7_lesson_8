from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['POST'])
def register_user_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = RegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.data.login_status = True
        serializer.data.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_view(request):
    users = UserModel.objects.all()
    serializer = UserModelSerializer(users, many=True)
