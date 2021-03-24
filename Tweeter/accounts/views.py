from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from django.contrib import messages
from project.models import Profile, Post
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


# Login page view
def login(request):
    return render(request, 'accounts/login.html')


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
    return render(request, 'accounts/register.html', {'form': form})


# Profile View
class ProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


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
