from django.test import TestCase, Client
from django.urls import reverse
from project.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class TestViews(TestCase):

    # Setup stuff for testing view pages
    # Storing info about urls and creating test user and test post
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.user1 = User.objects.create(
            username='Meng',
            password='tesing12345',
            email='email@gmail.com',
        )

        self.profile_url = reverse('profile-page', args=[1])
        self.post1 = Post.objects.create(

            content='test',
            author=self.user1,
            date_posted=timezone.now()
        )
        self.post_detail_url = reverse('post-page', args=[1])
        self.client.force_login(User.objects.get_or_create(username='Meng')[0])
        self.profile_follow_url = reverse('follow-user', args=[1])
        self.post_create_url = reverse('post-create')
        self.comment_create_url = reverse('comment-create', args=[1])
        self.delete_post_url = reverse('delete-post', args=[1])
        self.front_url = reverse('front-page')
        self.post_list_url = reverse('home-page')

    # Test login view page
    def test_login(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)

    # Test profile view page
    def test_profile_view(self):
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    # Test register view page
    def test_register(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    # Test post detail view page
    def test_post_detail_view(self):
        response = self.client.get(self.post_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_page.html')

    # Test post create view page
    def test_post_create_view(self):
        response = self.client.post(self.post_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')

    # Test comment create view page
    def test_comment_create_view(self):
        response = self.client.get(self.comment_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/add_comment.html')

    # Test delete post view page
    def test_delete_post_view(self):
        response = self.client.get(self.delete_post_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/delete_post.html')

    # Test front view page
    def test_front_view(self):
        response = self.client.get(self.front_url)

        self.assertEquals(response.status_code, 200)

    # Test post list view page
    def test_post_list_view(self):
        response = self.client.get(self.post_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/home.html')




