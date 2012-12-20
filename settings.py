# -*- coding:utf-8 -*-

# Django settings for fcpe63 project.


import os.path
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME = 'fcpe63'


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dominique Guardiola', 'web@quinode.fr'),
)
MANAGERS = ADMINS
TIME_ZONE = "Europe/Paris"
LANGUAGE_CODE = 'fr-FR'

USE_L10N = True
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr'
SITE_ID = 1
USE_I18N = True


import locale
locale.setlocale(locale.LC_ALL,'')
import django.conf.global_settings as DEFAULT_SETTINGS

DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET='utf-8'

AUTH_PROFILE_MODULE = 'fcpe.adherent'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

# Upload directory
MEDIA_ROOT = os.path.abspath(PROJECT_PATH + '/' + PROJECT_NAME + '/media/')
MEDIA_URL = '/media/'

# Static files
STATIC_ROOT = os.path.abspath(PROJECT_PATH + '/' + PROJECT_NAME + '/static_collected/')
STATIC_URL = '/static/'

# compat fix ?
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"


STATICFILES_DIRS = [
   # os.path.abspath(PROJECT_PATH + '/' + PROJECT_NAME + '/static/'),
]
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

TEMPLATE_DIRS = (
    os.path.abspath(PROJECT_PATH + '/' + PROJECT_NAME + '/templates/'),

    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

MIDDLEWARE_CLASSES = [
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
]

ROOT_URLCONF = 'fcpe63.urls'



INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.gis',
    'south',
    'oembed',
#    'adminbrowse',
    'django_mailman',
    'django_extensions',

    #coop_cms
    'sorl.thumbnail',
    'html_field',
    'taggit',
    'taggit_autocomplete_modified',
    'taggit_templatetags',
    'coop_cms',
    'coop_cms.apps.basic_cms',
    'djaloha',
    'colorbox',
    'coop_bar',
    'communes',
    'fcpe',
    'form_designer',
    'pagination',
    'tinymce',
    'raven',

]

JQUERY_JS = 'static/js/jquery-1.7.min.js'


TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'relative_urls': False,
    'width': '617px', 'height': '220px',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_buttons1': 'bold,italic,|,justifyleft,justifycenter,justifyright,|,bullist,numlist,|,link,unlink,|,code',
    'theme_advanced_buttons2': '', 'theme_advanced_buttons3': ''
    }


DJALOHA_LINK_MODELS = ('fcpe.Article',)
COOP_CMS_ARTICLE_CLASS = 'fcpe.models.Article'
COOP_CMS_ARTICLE_FORM = 'fcpe.admin.ArticleForm'

COOP_CMS_ARTICLE_TEMPLATES = (
    ('fcpe_article.html','Standard, résumé en chapeau'),
    ('fcpe_article_integre.html','Standard, résumé intégré'),
    ('fcpe_article_sans_logo.html','Sans logo, résumé en chapeau'),
    ('fcpe_article_sans_logo_integre.html','Sans logo, résumé intégré'),
    ('fcpe_home.html','Page d’accueil (spécial)')
    )
COOP_CMS_ARTICLE_LOGO_SIZE = '200'
COOP_BAR_MODULES = ('fcpe63.cms_coop_bar',)
COOP_CMS_NEWSLETTER_TEMPLATES = (('fcpe_newsletter.html', 'Lettre mensuelle'),)
COOP_CMS_FROM_EMAIL = '"FCPE 63" <contact@fcpe63.fr>'
COOP_CMS_TEST_EMAILS = ('"Dom" <contact@quinode.fr>',)
COOP_CMS_SITE_PREFIX = 'http://127.0.0.1:8000'

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
   'django.core.context_processors.request',
   'fcpe.context_processors.homepage_articles',
)

AUTHENTICATION_BACKENDS = DEFAULT_SETTINGS.AUTHENTICATION_BACKENDS + (
    'utils.email_auth.EmailBackend',
    'coop_cms.perms_backends.ArticlePermissionBackend',
 )


#ADMIN_TOOLS_MENU = 'base.menu.CustomMenu'
#ADMIN_TOOLS_INDEX_DASHBOARD = 'base.dashboard.CustomIndexDashboard'
#ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'base.dashboard.CustomAppIndexDashboard'
#ADMIN_TOOLS_THEMING_CSS = 'css/coop_theming.css'

#AUTOCOMPLETE_MEDIA_PREFIX = '/static/autocomplete/media/'
#ADMINBROWSE_MEDIA_URL= '/static/adminbrowse/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_NAME
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simplest': {
            'format': '%(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },

    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console-dumb': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simplest'
        },

    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },

}
try:
    from local_settings import *
except ImportError, exp:
    raise ImproperlyConfigured("Problem loading local_settings.py file : ", exp)


# debug settings : load dev tools (FireLogger & Django debug Toolbar) or setup Sentry Logging
try:
    DEBUG_SETTINGS = {'apps': INSTALLED_APPS,
                      'middleware': MIDDLEWARE_CLASSES,
                      'logging': LOGGING
                    }
    from debug_settings import *
except ImportError, exp:
    raise ImproperlyConfigured("Unable to find debug_settings.py file : ", exp)
