from django.views.generic import DetailView, CreateView, DeleteView
from project.models import Post, Comment
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from accounts.forms import CommentForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


# Detailed post view that is shown in the post page
@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_page.html'


# Post Create View
@method_decorator(login_required, name='dispatch')
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


# Comment View
@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user

        return super().form_valid(form)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('home-page')
