# -*- coding:utf-8 -*-

# Django settings for fcpe63 project.

import os
DIRNAME = os.path.dirname(__file__)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dominique Guardiola', 'web@quinode.fr'),
)
MANAGERS = ADMINS
TIME_ZONE = "Europe/Paris"
LANGUAGE_CODE = 'fr-FR'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'fcpe',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

import locale
locale.setlocale(locale.LC_ALL,'')
import django.conf.global_settings as DEFAULT_SETTINGS

DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET='utf-8'

AUTH_PROFILE_MODULE = 'fcpe.adherent'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'


MEDIA_ROOT = os.path.join(DIRNAME,'static/uploads/')
MEDIA_URL = '/static/uploads/'

STATIC_ROOT = os.path.join(DIRNAME,'static_collected/')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(DIRNAME,'static/'),
    #os.path.join(DIRNAME,'static/admin/'),
    #os.path.join(DIRNAME,'djaloha/static/'),
    #os.path.join(DIRNAME,'coop_cms/static/'),
    #os.path.join(DIRNAME,'/rss_sync/static/'),
    #os.path.abspath(ADMIN_TOOLS_PATH,'/media/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b^&97ode(=xw_ijk6v)4#31=5i^ezazfeoq#g1&^ksz9lv8w&a'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'fcpe63.urls'

TEMPLATE_DIRS = (
    os.path.join(DIRNAME+'/templates/'),    
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
#    'adminbrowse',
    'django_mailman',
    
    #coop_cms
    'livesettings',
    'sorl.thumbnail',
    'html_field',
    'taggit',
    'taggit_autocomplete_modified',
    'taggit_templatetags',
    'coop_cms',
    'djaloha',
    'communes',
    'fcpe',

)

LIVESETTINGS_OPTIONS = \
{
    1: {
    'DB': True,
       'SETTINGS': {
            u'coop_cms': {u'CONTENT_APPS': u'["coop_cms"]'}
        }
    }
}


#ADMIN_TOOLS_MENU = 'base.menu.CustomMenu'
#ADMIN_TOOLS_INDEX_DASHBOARD = 'base.dashboard.CustomIndexDashboard'
#ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'base.dashboard.CustomAppIndexDashboard'
#ADMIN_TOOLS_THEMING_CSS = 'css/coop_theming.css'

#AUTOCOMPLETE_MEDIA_PREFIX = '/static/autocomplete/media/'
#ADMINBROWSE_MEDIA_URL= '/static/adminbrowse/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = DEFAULT_SETTINGS.AUTHENTICATION_BACKENDS + (
    'utils.email_auth.EmailBackend',
 )

CACHE_MIDDLEWARE_KEY_PREFIX = DIRNAME
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

DJALOHA_LINK_MODELS = ('coop_cms.Article',)

LIVESETTINGS_OPTIONS = \
{
    1: {
    'DB': True,
       'SETTINGS': {
            u'coop_cms': {u'CONTENT_APPS': u'["coop_cms"]'}
        }
    }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


try:
    from local_settings import *
except ImportError, exp:
    pass
    
    