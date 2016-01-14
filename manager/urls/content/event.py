from django.conf.urls import patterns, include, url

from manager.views.content import Event

event = Event()

urlpatterns = patterns('',
	url(r'^see/(?P<event_id>\d+)/$', event.see, name="content_event_see"),
)