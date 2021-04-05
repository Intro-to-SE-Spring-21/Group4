from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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
@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'project/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['following'] = user.profile.following.all()
        return context


def search_results(request):
    if request.method == "POST":
        search = request.POST['search']
        posts = Post.objects.filter(content__contains=search)
        users = User.objects.filter(username__contains=search)
        return render(request, 'project/search.html', {'search': search, 'posts': posts, 'users': users})
    else:
        return render(request, 'project/home.html', {})
