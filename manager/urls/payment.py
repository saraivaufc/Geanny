from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^paypal/', include('paypal.standard.ipn.urls')),
)