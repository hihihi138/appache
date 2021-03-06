from django.conf.urls.defaults import *
from feeds import LatestVideosFeed

urlpatterns = patterns('',
    (r'^$', 'youku.views.video_list_page'),
    (r'^video/(\d{4})/(\d{2})/(\d{2})/(\d{6})/$', 'youku.views.video_page'),
    (r'^log/$', 'youku.views.log_page'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^category/([^/]+)/$', 'youku.views.category_page'),
    (r'^tag/([^/]+)/$', 'youku.views.tag_page'),
    (r'^rss/$', LatestVideosFeed()),
    (r'^post/$', 'youku.views.post_video'),
    (r'^post/thanks/$', 'youku.views.post_thanks'),
    (r'^super/posts$', 'youku.views.posted_videos'),
    (r'^suggestion/$', 'youku.views.suggestion'),
    (r'^suggestion/thanks/$', 'youku.views.suggestion_thanks'),
)
