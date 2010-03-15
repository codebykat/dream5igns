from django.conf.urls.defaults import *
import os.path

media_root = os.path.join(os.path.dirname(__file__),"media")

urlpatterns = patterns('',
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': media_root}),
    (r'mosaic', 'gallery.views.mosaic'),
    (r'felines', 'gallery.views.felines'),
    (r'tags', 'gallery.views.tags'),
    (r'', 'gallery.views.index'),
)
