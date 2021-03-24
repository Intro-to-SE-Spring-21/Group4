from django.views.generic import DetailView, CreateView
from project.models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# Detailed post view that is shown in the post page
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_page.html'


# Post Create View
class PostCreateView(CreateView):
    model = Post
    fields = ['content']
    template_name = 'posts/post_form.html'

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


# Like View
def like_post_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-page', args=[str(pk)]))


# Like View
def like_profile_post_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('profile-page', args=[str(pk)]))
