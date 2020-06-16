from django.conf.urls import url, include

from . import views

# Application Routes (URLs)

app_name = "voting"

urlpatterns = [
    # General Page Views
    url(r"^$", views.homepage_view, name="homepage"),
    url(r"^add-poll$", views.add_poll, name="add_poll"),
    url(r"^delete-poll/(?P<pk>\d+)/$", views.DeletePollView.as_view(), name="delete_poll"),
    url(r"^vote/(?P<result>\d+)/poll/(?P<poll>\d+)/$", views.vote_view, name="vote"),
]
