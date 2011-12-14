from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from fcpe import templatetags 

#from autocomplete.views import autocomplete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'coop_cms.views.view_article', kwargs={'url':'accueil'}, name='coop_cms_view_article'),
    url(r'^tag/(?P<slug>.*)/$', 'fcpe.views.tag', name='fcpe_tag'),

#    url('^autocomplete/', include(autocomplete.urls)),
#    url(r'^fcpe/', include('fcpe.urls')),
    (r'^settings/', include('livesettings.urls')),
    (r'^formulaire/', include('form_designer.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^taggit_autocomplete_modified/', include('taggit_autocomplete_modified.urls')),)

    
urlpatterns += staticfiles_urlpatterns()

import sys
from django.conf import settings
if settings.DEBUG or ('test' in sys.argv):
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    )
    
urlpatterns += patterns('',
    (r'^', include('coop_cms.urls')),
)    