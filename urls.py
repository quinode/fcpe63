from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from autocomplete.views import autocomplete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
#    url('^autocomplete/', include(autocomplete.urls)),
    #url(r'^$', 'fcpe63.views.home', name='home'),
    #url(r'^fcpe/', include('fcpe.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)

urlpatterns += staticfiles_urlpatterns()
