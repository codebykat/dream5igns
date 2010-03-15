from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from dream5igns.flickr.views import get_photos, get_tags

def index(request):
  photos = get_photos()

  return render_to_response('index.html', {'photos':photos})

def mosaic(request, tag="favorites"):
  try:
    tag = request.REQUEST['tag']
  except:
    tag = "favorites"
  photos = get_photos(tags=tag)
  return render_to_response('mosaic.html', {'photos':photos})

def tags(request):
  tags = get_tags()
  return render_to_response('tags.html', {'tags':tags})
