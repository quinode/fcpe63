# -*- coding:utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('fcpe.views',
    url(r'^conseil/([A-Z0-9]+)/$', 'fiche_conseil', name='fcpe_fiche_conseil'),
    url(r'^cartographie/$', 'carto', name='fcpe_carto'),
    url(r'^cartographie/json/$', 'conseils_geojson', name='fcpe_conseils_geojson'),
    )

