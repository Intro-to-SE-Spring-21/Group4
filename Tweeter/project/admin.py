from django.contrib import admin

from .models import Post, Profile, Comment

# This is the admin page where the admin can see the profiles and posts
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
