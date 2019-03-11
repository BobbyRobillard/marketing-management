from django.contrib import admin

from .models import Topic, Post, Platform, PostLocation

admin.site.register(Topic)
admin.site.register(Platform)
admin.site.register(Post)
admin.site.register(PostLocation)
