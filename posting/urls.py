from django.conf.urls import url, include

from . import views

# Application Routes (URLs)

app_name = 'posting'

urlpatterns = [
    	# General Page Views
		url(r'^$', views.homepage_view, name='homepage'),
		url(r'^add-post/(?P<pk>\d+)/$', views.add_post_view, name='add_post'),
]
