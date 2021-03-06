from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^c5/', include('c5.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^(?P<slug>[XAE0-9.+]+)/$', 'c5.dict.views.shapes'),
    (r'^(?P<voicetype>\w+)(?P<reading_id>\d+)/$', 'c5.dict.views.voicedict'),
)
