from django.urls import path

from .views import ListMinichua, DetailMinichua, ListTags, DetailTags

app_name = 'minichua'

urlpatterns = [
    path('', ListMinichua.as_view(), name='home'),
    path('<int:pk>/', DetailMinichua.as_view(), name='mini'),
    path('tag/', ListTags.as_view(), name='tags'),
]
