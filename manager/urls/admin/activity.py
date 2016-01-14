from django.conf.urls import patterns, include, url

from manager.views.admin import Activity

activity = Activity()

urlpatterns = patterns('',
	url(r'^see/(?P<activity_id>\d+)/$', activity.see, name="admin_activity_see"),
	url(r'^add/(?P<event_id>\d+)/$', activity.add, name="admin_activity_add"),
	url(r'^edit/(?P<activity_id>\d+)/$', activity.edit, name="admin_activity_edit"),
	url(r'^remove/(?P<activity_id>\d+)/$', activity.remove, name="admin_activity_remove"),
	
)