from django.contrib import admin

from .models import Project, StoreAuthentication

# Register your models here.
admin.site.register(Project)
admin.site.register(StoreAuthentication)
