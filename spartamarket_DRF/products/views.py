from django.shortcuts import  get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.urls import reverse
# from rest_framework.pagination import PageNumberPagination


# Create your views here.

@api_view(['GET', "POST"])
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        # paginator = PageNumberPagination()
        # paginator.page_size = 10  
        # result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, pk):
    if request.method == "GET":
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            return Response(serializer.data)
    
    elif request.method == "DELETE":
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
