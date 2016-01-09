from django.conf.urls import patterns, include, url
from django.contrib import admin
from geanny import settings

urlpatterns = patterns('',
	url(r'^', include('manager.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)

if 'rosetta' in settings.INSTALLED_APPS:
		urlpatterns += patterns('',
			url(r'^rosetta/', include('rosetta.urls')),
		)

if 'social.apps.django_app.default':
	urlpatterns += patterns('',
		url('', include('social.apps.django_app.urls', namespace='social')),
	)