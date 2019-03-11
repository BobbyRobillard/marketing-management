from django.conf.urls import url, include

from . import views

from administration.views import *

# Application Routes (URLs)

app_name = 'administration'

urlpatterns = [
    	# General Page Views
		url(r'^$', views.homepage_view, name='homepage'),
		# url(r'^show_posts/(?P<pk>\d+)/$', views.show_posts, name='show_posts'),
		url(r'^view-project/(?P<pk>\d+)/$', ViewProjectView.as_view(), name='view_project'),
		url(r'^view-project-posts/(?P<project>\d+)/(?P<topic>\d+)/$', ViewProjectPosts.as_view(), name='view_project_posts'),
		url(r'^view-post-locations/(?P<project>\d+)/(?P<topic>\d+)/(?P<post>\d+)$', ViewPostLocations.as_view(), name='view_post_locations'),
		url(r'^add-project$', AddProjectView.as_view(), name='add_project'),
		url(r'^financial-summary/(?P<pk>\d+)/$', views.financial_summary_view, name='financial_summary'),
		url(r'^update-project/(?P<pk>\d+)/$', UpdateProjectView.as_view(), name='update_project'),
		url(r'^delete-project/(?P<pk>\d+)/$', views.delete_project, name='delete_project'),
]
