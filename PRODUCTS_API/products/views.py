from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Product_serializer
from .models import Product

@api_view(['GET'])
def products_list(request):
  products = Product.objects.all()
  serializer = Product_serializer(products, many = True)


  return Response(serializer.data)

@api_view('GET')
def product_detail(requst, pk):
  print(pk)
  return Response(pk)