from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name = 'front-page'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
]