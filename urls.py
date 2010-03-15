from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dream5igns/', include('dream5igns.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),  # django 1.1.1
    (r'^admin/', admin.site.root),  # django 1.0.2

    (r'image_cache/', include('dream5igns.flickr.urls')),
    (r'', include('dream5igns.gallery.urls')),
)
