from django.shortcuts import render
from rest_framework import generics

from minichua import models
from .serialzers import MiniSerializer, TagsSerializer

class ListMinichua(generics.ListCreateAPIView):
    queryset = models.Mini.objects.all()
    serializer_class = MiniSerializer

class DetailMinichua(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mini.objects.all()
    serializer_class = MiniSerializer

class ListTags(generics.ListCreateAPIView):
    queryset = models.Tags.objects.all()
    serializer_class = TagsSerializer

class DetailTags(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tags.objects.all()
    serializer_class = TagsSerializer