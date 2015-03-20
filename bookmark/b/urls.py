from django.conf.urls import patterns, url, include
from tastypie.api import Api

from b.api import BookmarkResource

v1_api = Api(api_name='v1')
v1_api.register(BookmarkResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)
