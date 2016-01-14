from django.conf.urls import patterns, include, url

from manager.views.index import Index

index = Index()

urlpatterns = patterns('',
	url(r'^$', index.admin, name="admin"),
    url(r'^event/', include('manager.urls.admin.event')),
    url(r'^activity/', include('manager.urls.admin.activity')),
)