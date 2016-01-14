from django.conf.urls import patterns, include, url

from manager.views.index import Index

index = Index()

urlpatterns = patterns('',
	url(r'^', include('manager.urls.content')),
	url(r'^admin/', include('manager.urls.admin')),
    url(r'^accounts/', include('manager.urls.accounts')),
    url(r'^something/', include('manager.urls.payment')),
)