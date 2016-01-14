from django.conf.urls import patterns, include, url

from manager.views.admin import Resource

resource = Resource()

urlpatterns = patterns('',
	url(r'^see/(?P<resource_id>\d+)/$', resource.see, name="admin_resource_see"),
	url(r'^add/(?P<event_id>\d+)/$', resource.add, name="admin_resource_add"),
	url(r'^edit/(?P<resource_id>\d+)/$', resource.edit, name="admin_resource_edit"),
	url(r'^remove/(?P<resource_id>\d+)/$', resource.remove, name="admin_resource_remove"),
	
)