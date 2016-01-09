from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^', include('manager.urls.index')),
    url(r'^index/', include('manager.urls.index')),
    url(r'^accounts/', include('manager.urls.accounts')),
)