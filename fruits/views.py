from django.shortcuts import render
from rest_framework import generics
from .models import Fruit
from .serializer import FruitSerializer

# Create your views here.

class FruitsList(generics.ListCreateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

class FruitDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer


