from django.shortcuts import render
from rest_framework import generics
from config.pagination import CustomPagination

from minichua import models
from .serialzers import MiniSerializer, TagsSerializer

class ListMinichua(generics.ListCreateAPIView):
    queryset = models.Mini.objects.all()
    serializer_class = MiniSerializer
    pagination_class = CustomPagination
    filterset_fields = ['tags']

class DetailMinichua(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mini.objects.all()
    serializer_class = MiniSerializer
    template_name = 'detail.html'
    filterset_fields = ['tags']

class ListTags(generics.ListCreateAPIView):
    queryset = models.Tags.objects.all()
    serializer_class = TagsSerializer

class DetailTags(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tags.objects.all()
    serializer_class = TagsSerializer