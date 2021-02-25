from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from .forms import UserRegisterForm
from .models import Post

# Create your views here.
def front(request):
    return render(request, 'project/front.html')

def login(request):
    return render(request, 'project/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # get username
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'project/register.html', {'form': form})

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'project/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'project/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.likes = 0
        return super().form_valid(form)


