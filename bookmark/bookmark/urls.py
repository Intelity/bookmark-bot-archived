from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookmark.views.home', name='home'),
    url(r'^', include('b.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
