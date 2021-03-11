from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    content = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='Tweeter_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('home-page')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='Following', blank=True)
    followers = models.ManyToManyField(User, related_name='Followers', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


