from django.shortcuts import render
from rest_framework import generics
from config.pagination import CustomPagination

from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

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

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserProfileView(generic.DetailView):
    model = User
    template_name = 'user_profile.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])