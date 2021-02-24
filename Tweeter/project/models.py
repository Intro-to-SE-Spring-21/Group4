from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    content = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField()

    def __str__(self):
        return self.content
