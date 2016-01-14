from django.conf.urls import patterns, include, url

from manager.views.admin import Event

event = Event()

urlpatterns = patterns('',
	url(r'^see/(?P<event_id>\d+)/$', event.see, name="admin_event_see"),
	url(r'^add/$', event.add, name="admin_event_add"),
	url(r'^edit/(?P<event_id>\d+)/$', event.edit, name="admin_event_edit"),
	url(r'^remove/(?P<event_id>\d+)/$', event.remove, name="admin_event_remove"),
	
)