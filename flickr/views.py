from urllib import urlopen
import os
try:
  import json
except:
  import simplejson as json

try:
  from flickr_settings import *
  API_KEY
except:
  raise Warning, "ERROR: Please set your API key and username in flickr_settings.py."

media_root = os.path.join(os.path.dirname(__file__),"media")

def get_userid(username):
  print "called"
  method = 'flickr.people.findByUsername'
  url = '%s%s' % (HOST, API) 
  query = 'api_key=%s&method=%s&format=%s' % (API_KEY, method, "json")
  query += '&username=%s&nojsoncallback=1' % USERNAME
  response = json.load(urlopen(url, query))
  username = ""
  if response['stat'] == "ok":
    username = response['user']['nsid']
  return username

def get_tags():
  try: userid = USER_ID
  except: userid = get_userid(USERNAME)

  tags = []
  method = 'flickr.tags.getListUser'
  url = '%s%s' % (HOST, API) 
  query = 'api_key=%s&method=%s&format=%s' % (API_KEY, method, "json")
  query += '&user_id=%s&nojsoncallback=1' % USER_ID
  response = json.load(urlopen(url, query))
  if response['stat'] != "ok":
    return []

  tags = response["who"]["tags"]["tag"]
  tags = [tag['_content'] for tag in tags]
  print tags
  return tags

def get_photos(tags=TAGS):
  try: userid = USER_ID
  except: userid = get_userid(USERNAME)

  photos = []

  method = 'flickr.photos.search'

  url = '%s%s' % (HOST, API)
  query = 'user_id=%s&tags=%s&per_page=100' % (userid, tags)
  query += '&api_key=%s&method=%s&format=%s' % (API_KEY, method, "json")

  try:
    query += '&sort=%s' % SORT
  except: pass
  try:
    query += '&tag_mode=%s' % TAGMODE
  except: pass

  query += '&nojsoncallback=1'
  query += '&extras=url_sq,url_m,date_taken,description'

  response = json.load(urlopen(url, query))
  if response['stat'] != "ok":
    return []

  photos = response["photos"]["photo"]

  # load other pages if we need to
  # (but only if we have tags, we can't load the whole photostream)
  if tags != "":
    pgs = response['photos']['pages']
    for i in range(2, pgs+1):
      response = json.load(urlopen(url, query+"&page=%s" % i))
      if response['stat'] != "ok":
        return []
      photos.extend(response["photos"]["photo"])

  # update links
  for photo in photos:
    add_photo_links(photo)
    #cache_images(photo)

  return photos

def add_photo_links(photo):
  photo['thumbnail'] = photo['url_sq']
  photo['src'] = photo['url_m']
  photo['description'] = photo['description']['_content']
  #photo['thumbnail'] = "http://farm%s.static.flickr.com/%s/%s_%s_s.jpg" % \
  #       (photo['farm'], photo['server'], photo['id'], photo['secret'])
  #photo['src'] = "http://farm%s.static.flickr.com/%s/%s_%s.jpg" % \
  #       (photo['farm'], photo['server'], photo['id'], photo['secret'])
  photo['url'] = "http://www.flickr.com/photos/%s/%s" % \
                 (USERNAME, photo['id'])
  return

def cache_images(photo):
  # TODO separate folders for separate tags
  thumbdir = media_root + "/images/thumbs/"

  # if thumbnail already exists, no need to cache it
  try:
    file = open(thumbdir + photo['id'] +".jpg", "rb")
  except:
    img = urlopen(photo['thumbnail'])
    file = open(thumbdir + photo['id']+".jpg", "wb")
    file.write(img.read())
    file.close()

  photo['thumbnail'] = "image_cache/thumbs/" + photo['id'] + ".jpg"

  imgdir = media_root + "/images/medium/"

  # if image already exists, no need to cache it
  try:
    file = open(imgdir + photo['id'] +".jpg", "rb")
  except:
    img = urlopen(photo['src'])
    file = open(imgdir + photo['id']+".jpg", "wb")
    file.write(img.read())
    file.close()

  photo['src'] = "image_cache/medium/" + photo['id'] + ".jpg"

  return

# TODO: how to clear out unused cached images?  

#def photo_search(user_id=USER_ID, tags=TAGS, per_page='', page='',
#                 extras='', content_type=''):
