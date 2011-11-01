from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from autocomplete.views import autocomplete
    
    

urlpatterns = patterns('',
    url('^autocomplete/', include(autocomplete.urls)),
    url(r'^newsletters/', include('emencia.django.newsletter.urls')),
    #url(r'^$', 'fcpe63.views.home', name='home'),
    #url(r'^fcpe/', include('fcpe.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
