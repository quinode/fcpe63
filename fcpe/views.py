# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
#from taggit.models import Tag
from django.contrib.auth.models import User
from django.conf import settings
from fcpe.models import ConseilLocal
from taggit.models import Tag
from fcpe.models import Article
import json


def home(request):
    rdict = {}
    rdict['home_page_articles'] = Article.objects.filter(accueil=True).order_by('priorite', '-created')
    print rdict
    return render_to_response('index.html', rdict, RequestContext(request))


def tag(request, slug):
    rdict = {}
    rdict['tag'] = get_object_or_404(Tag, slug=slug)
    rdict['articles'] = Article.objects.filter(tags__slug__in=[slug])
    return render_to_response('tag.html', rdict, RequestContext(request))


def carto(request):
    liste_conseils = []
    qs = ConseilLocal.objects.filter(code__istartswith="063").exclude(commune=None).exclude(code="0634Z0090").order_by('commune__nom')
    for cl in qs:
        liste_conseils.append({"nom": cl.nom, "url": cl.get_absolute_url(), "commune": cl.commune.nom})
    return render_to_response('carto.html', {"liste_conseils": liste_conseils}, RequestContext(request))


def fiche_conseil(request, code):
    conseil = get_object_or_404(ConseilLocal, code=code)
    return render_to_response('conseil.html', {'conseil': conseil}, context_instance=RequestContext(request))


def conseils_geojson(request):
    communes = {}
    qs = ConseilLocal.objects.filter(code__istartswith="063").exclude(commune=None).exclude(code="0634Z0090")
    for cl in qs:
        if not cl.commune_id in communes:
            communes[cl.commune_id] =  {
                "type": "Feature",
                "properties": {
                    "name": cl.commune.nom,
                    "popupContent": u"<h4>" + cl.commune.nom + "</h4><p class='clocal'><a href='" + cl.get_absolute_url() + u"'>" + cl.nom + "</a></p>"
                    },
                "geometry": {
                    "type": "Point",
                    "coordinates": [cl.commune.longitude, cl.commune.latitude]
                    }
                }
        else:
            communes[cl.commune_id]["properties"]["popupContent"] += u"\n<p class='clocal'><a href='" + \
                        cl.get_absolute_url() + u"'>" + cl.nom + "</a></p>"
    conseils = { "type": "FeatureCollection", "features": communes.values() }
    return HttpResponse(json.dumps(conseils), mimetype="application/json")


