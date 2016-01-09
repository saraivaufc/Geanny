from django.conf.urls import patterns, include, url

from manager.views.index import Index

index = Index()

urlpatterns = patterns('',
	url(r'^$', index.home),
	url(r'^home/$', index.home, name="home"),
)
