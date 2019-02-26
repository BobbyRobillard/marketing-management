from django.contrib import admin

from .models import Topic, Post, Platform

admin.site.register(Topic)
admin.site.register(Platform)
admin.site.register(Post)
