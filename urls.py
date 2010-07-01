from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout

import os

urlpatterns = patterns('',
    (r'^$', 'youku.views.video_list_page'),
    (r'^video/(\d{4})/(\d{2})/(\d{2})/(\d{6})/$', 'youku.views.video_page'),
    (r'^log/$', 'youku.views.log_page'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^category/([^/]+)/$', 'youku.views.category_page'),
    (r'^tag/([^/]+)/$', 'youku.views.tag_page'),
    # admin related
    (r'^admin/', include(admin.site.urls)),
	(r'^accounts/',  include('registration.backends.default.urls')),
    # static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(os.path.abspath(__file__)) + '/static/'}),
)
