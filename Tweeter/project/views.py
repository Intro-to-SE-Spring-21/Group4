from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from .forms import UserRegisterForm
from .models import Post, Profile
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


# List of views

# Front page view
def front(request):
    return render(request, 'project/front.html')


# Login page view
def login(request):
    return render(request, 'project/login.html')


# Register page view
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


# Detailed post view that is shown in the post page
class PostDetailView(DetailView):
    model = Post
    template_name = 'project/post_page.html'


# Post Create View
class PostCreateView(CreateView):
    model = Post
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


# Like View
def like_view(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('home-page'))


# Profile View
class ProfileView(DetailView):
    model = Profile
    template_name = 'project/profile.html'


# Profile Follow View
def profile_follow_view(request, pk):

    # currently logged in user
    user_profile = get_object_or_404(Profile, id=request.user.profile.id)

    # profile the user is currently looking at
    profile = get_object_or_404(Profile, id=request.POST.get('profile_id'))

    # if the user is currently following the profile:
    #   remove the profile from the user's following list
    #   remove the user from the profile's follower list
    if profile.followers.filter(id=request.user.id).exists():
        user_profile.following.remove(profile.user)
        profile.followers.remove(request.user)

    # otherwise
    #   add the profile to the user's following list
    #   add the user to the profile's follower list
    else:
        user_profile.following.add(profile.user)
        profile.followers.add(request.user)

    # redirect user to current profile page
    return HttpResponseRedirect(reverse('profile-page', args=[str(pk)]))


# Like View
def like_post_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-page', args=[str(pk)]))

