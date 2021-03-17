from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    like_view,
    ProfileView,
    profile_follow_view,
    like_post_view,
)

# List of urls that redirects user to their desired destination
urlpatterns = [
    path('', views.front, name='front-page'),
    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='project/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('home/', PostListView.as_view(), name='home-page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-page'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('like/', like_view, name='like-post'),
    path('post/like/<int:pk>/', like_post_view, name='like-post-page'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile-page'),
    path('profile/follow/<int:pk>', profile_follow_view, name='follow-user')
]