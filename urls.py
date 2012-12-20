from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView

class TextPlainView(TemplateView):
    def render_to_response(self, context, **kwargs):
        return super(TextPlainView, self).render_to_response(
              context, content_type='text/plain', **kwargs)


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from fcpe import templatetags

handler500 = 'views.SentryHandler500'

from feeds import FluxRSS

#from autocomplete.views import autocomplete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'coop_cms.views.view_article', kwargs={'url': 'accueil'}, name='coop_cms_view_article'),
    url(r'^tag/(?P<slug>.*)/$', 'fcpe.views.tag', name='fcpe_tag'),

#    url('^autocomplete/', include(autocomplete.urls)),
#    url(r'^fcpe/', include('fcpe.urls')),
    url(r'^formulaire/', include('form_designer.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^taggit_autocomplete_modified/', include('taggit_autocomplete_modified.urls')),
    url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/fcpe/favicon.ico')),

    (r'^accounts/', include('django.contrib.auth.urls')),
    (r'^rss/$', FluxRSS()),

    )

import sys
from django.conf import settings

# for local testing
if settings.DEBUG or ('test' in sys.argv) or ('runserver' in sys.argv):
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )


urlpatterns += patterns('',
    (r'^', include('fcpe.urls')),
    (r'^djaloha/', include('djaloha.urls')),
    (r'^', include('coop_cms.urls')),
)

