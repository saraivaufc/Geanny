from django.conf.urls import patterns, include, url

from manager.views.content import Activity

activity = Activity()

urlpatterns = patterns('',
	url(r'^see/(?P<activity_id>\d+)/$', activity.see, name="content_activity_see"),
)