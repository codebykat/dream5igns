from django.conf.urls.defaults import *
import os.path

media_root = os.path.join(os.path.dirname(__file__),"media/images")

urlpatterns = patterns('',
    (r'^(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': media_root}),
)
