from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from dream5igns.flickr.views import get_photos

def index(request):
  photos = get_photos()

  return render_to_response('index.html', {'photos':photos})
