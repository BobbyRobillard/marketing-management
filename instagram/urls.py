from django.conf.urls import url, include

from . import views

app_name = "instagram"

urlpatterns = [
    # General Page Views
    url(r"^$", views.homepage, name="homepage"),
]
