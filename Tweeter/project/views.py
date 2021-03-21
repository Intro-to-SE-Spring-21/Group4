from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# List of views

# Front page view
def front(request):
    return render(request, 'project/front.html')


# possibly unused
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'project/home.html', context)


# Post-list view that displays posts on the home page
class PostListView(ListView):
    model = Post
    template_name = 'project/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

