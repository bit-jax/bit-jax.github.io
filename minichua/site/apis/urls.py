from django.urls import path

from .views import ListMinichua, DetailMinichua

urlpatterns = [
    path('', ListMinichua.as_view()),
    path('<int:pk>/', DetailMinichua.as_view()),
]
