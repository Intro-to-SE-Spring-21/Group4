from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.contrib.auth.models import User

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


def search_results(request):
    if request.method == "POST":
        search = request.POST['search']
        posts = Post.objects.filter(content__contains=search)
        users = User.objects.filter(username__contains=search)
        return render(request, 'project/search.html', {'search': search, 'posts': posts, 'users': users})
    else:
        return render(request, 'project/home.html', {})
