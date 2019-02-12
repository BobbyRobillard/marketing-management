from django.contrib import admin

from .models import Topic, Post, ApplicableCode

admin.site.register(ApplicableCode)
admin.site.register(Topic)
admin.site.register(Post)
