from django.shortcuts import render
from django.core import serializers
from rest_framework.response import Response
from .models import User
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.
@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def login(request):
    pass