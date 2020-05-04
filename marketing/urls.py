from django.conf.urls import url, include

from . import views

app_name = "marketing"

urlpatterns = [
    url(r"^$", views.homepage_view, name="homepage")
]
