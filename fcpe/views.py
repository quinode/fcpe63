# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404,redirect
#from taggit.models import Tag
from django.contrib.auth.models import User

from taggit.models import Tag
from fcpe.models import Article

def home(request):
    rdict ={}
    return render_to_response('index.html',rdict,RequestContext(request))

def tag(request, slug):
    rdict = {}
    rdict['tag'] = get_object_or_404(Tag, slug=slug)
    rdict['articles'] = Article.objects.filter(tags__slug__in=[slug])
    return render_to_response('tag.html',rdict,RequestContext(request))
