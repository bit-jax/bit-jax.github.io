from django.shortcuts import render
from rest_framework import generics

from minichua import models
from .serialzers import MiniSerializer

class ListMinichua(generics.ListCreateAPIView):
    queryset = models.Mini.objects.all()
    serializer_class = MiniSerializer

class DetailMinichua(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mini.objects.all()
    serializer_class = MiniSerializer
