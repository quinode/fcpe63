# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404,redirect
#from taggit.models import Tag
from django.contrib.auth.models import User


#from videos.models import Video,Commande

def home(request):
    rdict ={}
    return render_to_response('index.html',rdict,RequestContext(request))
