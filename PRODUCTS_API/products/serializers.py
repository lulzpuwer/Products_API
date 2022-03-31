from rest_framework import serializers
from .models import Product


class Product_serializer(serializers.ModelSerializer):
  class meta:
    model = Product
    fields = ['id','title', 'description', 'price', 'inventory_quality']