"""Tweeter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as user_views
from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('post/<int:pk>/', post_views.PostDetailView.as_view(), name='post-page'),
    path('post/new/', post_views.PostCreateView.as_view(), name='post-create'),
    path('like/', post_views.like_view, name='like-post'),
    path('post/like/<int:pk>/', post_views.like_post_view, name='like-post-page'),
    path('post/like/profile/<int:pk>/', post_views.like_profile_post_view, name='like-profile-post-page'),
    path('profile/<int:pk>', user_views.ProfileView.as_view(), name='profile-page'),
    path('profile/follow/<int:pk>', user_views.profile_follow_view, name='follow-user'),
    path('post/<int:pk>/comment/new/', post_views.CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/delete/', post_views.DeletePostView.as_view(), name='delete-post'),
]
