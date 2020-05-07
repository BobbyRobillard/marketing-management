from django.conf.urls import url, include

from . import views

app_name = "marketing"

urlpatterns = [
    url(r"^$", views.homepage_view, name="homepage"),
    url(r"^locations$", views.locations_view, name="locations"),
    url(r"^sample-posts$", views.sample_posts_view, name="sample_posts"),
    url(r"^live-posts$", views.live_posts_view, name="live_posts"),
    url(r"^tasks/(?P<status>\d+)/$", views.tasks_view, name="tasks"),
]
