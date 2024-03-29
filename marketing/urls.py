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
    url(r"^view-location/(?P<pk>\d+)/$", views.ViewLocationDetailView.as_view(), name="view_location"),

    # url(r"^add-sample-post$", views.CreateSamplePostView.as_view(), name="add_sample_post"),
    url(r"^sample-posts$", views.sample_posts_view, name="sample_posts"),
    url(r"^add-sample-posts$", views.CreateSamplePostView.as_view(), name="add_sample_post"),
    url(r"^delete-sample-post/(?P<pk>\d+)/$", views.DeleteSamplePostView.as_view(), name="delete_sample_post"),
    url(r"^view-sample-post/(?P<pk>\d+)/$", views.ViewSamplePostDetailView.as_view(), name="view_sample_post"),

    url(r"^live-posts$", views.live_posts_view, name="live_posts"),
    url(r"^create-live-post/(?P<pk>\d+)/$", views.CreateLivePostView.as_view(), name="create_live_post"),
    url(r"^mark-post-inactive/(?P<pk>\d+)/$", views.mark_post_inactive, name="mark_post_inactive"),
    url(r"^delete-live-post/(?P<pk>\d+)/$", views.DeleteLivePostView.as_view(), name="delete_live_post"),

    url(r"^resources$", views.resources_view, name="resources"),
    url(r"^add-resource$", views.CreateResourceView.as_view(), name="add_resource"),
    url(r"^delete-resource/(?P<pk>\d+)/$", views.DeleteResourceView.as_view(), name="delete_resource"),
    url(r"^view-resource/(?P<pk>\d+)/$", views.ViewResourceDetailView.as_view(), name="view_resource"),

    url(r"^tasks$", views.tasks_view, name="tasks"),

    url(r"^assign-post-task$", views.CreatePostingTaskView.as_view(), name="add_posting_task"),
    url(r"^mark-post-task-complete/(?P<pk>\d+)/$", views.mark_post_task_complete, name="mark_post_task_complete"),
    url(r"^delete-create-post-task/(?P<pk>\d+)/$", views.DeleteCreatePostTaskView.as_view(), name="delete_create_post_task"),
    url(r"^view-post-task/(?P<pk>\d+)/$", views.ViewPostTaskDetailView.as_view(), name="view_posting_task"),

    url(r"^assign-monitor-task$", views.CreateMonitoringTaskView.as_view(), name="add_monitoring_task"),
    url(r"^mark-monitor-task-complete/(?P<pk>\d+)/$", views.mark_monitor_task_complete, name="mark_monitor_task_complete"),
    url(r"^delete-monitor-post-task/(?P<pk>\d+)/$", views.DeleteMonitorPostTaskView.as_view(), name="delete_monitor_post_task"),
    url(r"^view-monitor-task/(?P<pk>\d+)/$", views.ViewMonitorTaskDetailView.as_view(), name="view_monitor_task"),
]
