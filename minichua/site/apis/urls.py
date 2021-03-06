from django.urls import path

from . import views

app_name = 'mini_api'

urlpatterns = [
    path('', views.ListMinichua.as_view(), name='home'),
    path('<int:pk>/', views.DetailMinichua.as_view(), name='mini'),
    path('tag/', views.ListTags.as_view(), name='tags'),
    path('tag/<int:pk>', views.DetailTags.as_view()),
    path('signup/', views.SignupView.as_view(), name='signup'),
    # path('all/', views.ListMinichua.as_view(), name='all'),
    ]
