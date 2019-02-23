from django.conf.urls import url, include

from . import views

# Application Routes (URLs)

app_name = 'posting'

urlpatterns = [
    	# General Page Views
		url(r'^$', views.homepage_view, name='homepage'),
		url(r'^add-post/(?P<pk>\d+)/$', views.add_post_view, name='add_post'),
		url(r'^update-post/(?P<pk>\d+)/$', views.update_post_view, name='update_post'),
		url(r'^add-codes-to-post/(?P<pk>\d+)/$', views.add_codes_to_post_view, name='add_codes_to_post'),
		url(r'^use-codes/(?P<pk>\d+)/$', views.use_codes_view, name='use_codes'),
		url(r'^remove-code/(?P<pk>\d+)/$', views.remove_coupon_view, name='remove_coupon'),
]
