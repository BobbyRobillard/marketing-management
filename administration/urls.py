from django.conf.urls import url, include

from . import views

from administration.views import (ViewProjectView, UpdateProjectView,
AddProjectView)

# Application Routes (URLs)

app_name = 'administration'

urlpatterns = [
    	# General Page Views
		url(r'^$', views.homepage_view, name='homepage'),
		url(r'^view-project/(?P<pk>\d+)/$', ViewProjectView.as_view(), name='view_project'),
		url(r'^add-project$', AddProjectView.as_view(), name='add_project'),
		url(r'^update-project/(?P<pk>\d+)/$', UpdateProjectView.as_view(), name='update_project'),
		url(r'^delete-project/(?P<pk>\d+)/$', views.delete_project, name='delete_project'),
]
