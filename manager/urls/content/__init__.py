from django.conf.urls import patterns, include, url

from manager.views.index import Index

index = Index()

urlpatterns = patterns('',
	url(r'^$', index.content, name="content"),
    url(r'^event/', include('manager.urls.content.event')),
    url(r'^activity/', include('manager.urls.content.activity')),
)