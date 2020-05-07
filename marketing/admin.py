from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Platform)
admin.site.register(CurrentProject)
admin.site.register(Location)
