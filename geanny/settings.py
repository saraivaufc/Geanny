"""
Django settings for geanny project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext_lazy as _


#Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf import global_settings
import os, sys
from imp import reload
reload(sys)
sys.setdefaultencoding('utf-8')


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)

from .social import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f!yoloe#v964g!#2gbie+6t)jh1##f&(89^afrl76ia%zcggu='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

DJANGO_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
	'rosetta',
	'nocaptcha_recaptcha',
	'social.apps.django_app.default',
)

LOCAL_APPS = (
	'manager',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

#Templates
TEMPLATE_DIRS = (
	'manager/templates',
	'manager/templates/manager/accounts',
	'nocaptcha_recaptcha/templates',
)


#TEMPLATE_CONTEXT
TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.tz',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
	'social.apps.django_app.context_processors.backends',
	'social.apps.django_app.context_processors.login_redirect',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
	"django.core.context_processors.request",
)

# Keep templates in memory
# TEMPLATE_LOAFAjango.template.loaders.app_directories.Loader',
#     )),
# )



MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#Message
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'


ROOT_URLCONF = 'geanny.urls'

WSGI_APPLICATION = 'geanny.wsgi.application'

#Authentication
AUTHENTICATION_BACKENDS = (
	'social.backends.facebook.FacebookOAuth2',
	'social.backends.google.GoogleOAuth2',
	'social.backends.twitter.TwitterOAuth',
	'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'auth.User'

LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'

#Recaptca
NORECAPTCHA_SITE_KEY  = "6LdVnQ0TAAAAAAwnuLsezpZwIRFhdqs-yrwdmG3n"
NORECAPTCHA_SECRET_KEY = "6LdVnQ0TAAAAAGtLXaOALJ6KTM4XvUF_bUg8enIc" 



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LOCALE_PATHS = (
	os.path.join(PROJECT_DIR, '../manager/locale'),
	'/var/local/translations/locale',
)

LANGUAGES = (
	 ('pt_BR', _('Brazilian Portuguese')),
	 ('en', _('English')),
	 ('es', _('Spanish')),
)


LANGUAGE_CODE = 'pt_BR'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT= os.path.join(PROJECT_DIR, '../media')
MEDIA_URL='/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, '.')
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, '../manager/static'),)

