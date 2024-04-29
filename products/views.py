from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status,generics
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class ProductListAPIView(generics.ListCreateAPIView):
# class ProductListAPIView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    @permission_classes([IsAuthenticated])
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    # def get(self,request):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)

class ProductDetailAPIView(APIView):
    pass