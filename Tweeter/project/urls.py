from django.urls import path
from . import views
from .views import PostListView


# List of urls that redirects user to their desired destination
urlpatterns = [
    path('', views.front, name='front-page'),
    path('home/', PostListView.as_view(), name='home-page'),
]