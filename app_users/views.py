from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        data = request.data
        serializer = RegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)