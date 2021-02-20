from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.front, name = 'front-page'),
    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name = 'login'),
    path('logout/', auth_views.LoginView.as_view(template_name='project/logout.html'), name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('home/', views.home, name = 'home-page'),
]