from django.test import SimpleTestCase
from django.urls import reverse, resolve
from project.views import PostListView, search_results, front
from accounts.views import register, ProfileView, profile_follow_view
from posts.views import PostDetailView, PostCreateView, like_view, like_post_view, like_profile_post_view, CommentCreateView, DeletePostView
from django.contrib.auth.views import LoginView, LogoutView


class TestUrls(SimpleTestCase):

    def test_front_url_is_resolved(self):
        url = reverse('front-page')
        self.assertEquals(resolve(url).func, front)

    def test_search_url_is_resolved(self):
        url = reverse('search-result')
        self.assertEquals(resolve(url).func, search_results)

    def test_home_url_is_resolved(self):
        url = reverse('home-page')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_profileview_url_is_resolved(self):
        url = reverse('profile-page', args=[1])
        self.assertEquals(resolve(url).func.view_class, ProfileView)

    def test_profilefollowview_url_is_resolved(self):
        url = reverse('follow-user', args=[1])
        self.assertEquals(resolve(url).func, profile_follow_view)

    def test_postdetailview_url_is_resolved(self):
        url = reverse('post-page', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_postcreateview_url_is_resolved(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_likeview_url_is_resolved(self):
        url = reverse('like-post')
        self.assertEquals(resolve(url).func, like_view)

    def test_likepostview_url_is_resolved(self):
        url = reverse('like-post-page', args=[1])
        self.assertEquals(resolve(url).func, like_post_view)

    def test_likeprofilepostview_url_is_resolved(self):
        url = reverse('like-profile-post-page', args=[1])
        self.assertEquals(resolve(url).func, like_profile_post_view)

    def test_commentcreateview_url_is_resolved(self):
        url = reverse('comment-create', args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentCreateView)

    def test_deletepostview_url_is_resolved(self):
        url = reverse('delete-post', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeletePostView)