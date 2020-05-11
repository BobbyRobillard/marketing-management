from django.conf.urls import url, include

from . import views

app_name = "marketing"

urlpatterns = [
    url(r"^$", views.homepage_view, name="homepage"),

    url(r"^add-project$", views.CreateProjectView.as_view(), name="add_project"),
    url(r"^set-current-project/(?P<pk>\d+)/$", views.set_current_project_view, name="set_current_project"),

    url(r"^add-location$", views.CreateLocationView.as_view(), name="add_location"),
    url(r"^locations$", views.locations_view, name="locations"),
    url(r"^delete-location/(?P<pk>\d+)/$", views.DeleteLocationView.as_view(), name="delete_location"),

    # url(r"^add-sample-post$", views.CreateSamplePostView.as_view(), name="add_sample_post"),
    url(r"^sample-posts$", views.sample_posts_view, name="sample_posts"),
    url(r"^add-sample-posts$", views.CreateSamplePostView.as_view(), name="add_sample_post"),
    url(r"^delete-sample-post/(?P<pk>\d+)/$", views.DeleteSamplePostView.as_view(), name="delete_sample_post"),

    url(r"^live-posts$", views.live_posts_view, name="live_posts"),

    url(r"^resources$", views.resources_view, name="resources"),
    url(r"^add-resource$", views.CreateResourceView.as_view(), name="add_resource"),
    url(r"^delete-resource/(?P<pk>\d+)/$", views.DeleteResourceView.as_view(), name="delete_resource"),

    url(r"^tasks$", views.tasks_view, name="tasks"),
    url(r"^assign-post-task$", views.CreatePostingTaskView.as_view(), name="add_posting_task"),
    url(r"^mark-task-complete/(?P<pk>\d+)/$", views.mark_task_complete_view, name="mark_task_complete"),
    url(r"^delete-task/(?P<pk>\d+)/$", views.DeleteTaskView.as_view(), name="delete_task"),
]
