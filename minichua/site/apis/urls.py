from django.urls import path

from .views import ListMinichua, DetailMinichua, ListTags, DetailTags

urlpatterns = [
    path('', ListMinichua.as_view()),
    path('<int:pk>/', DetailMinichua.as_view()),
    path('tag/', ListTags.as_view()),
]
