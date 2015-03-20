from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization

from b.models import Bookmark, Tag

class BookmarkResource(ModelResource):
    class Meta:
        queryset = Bookmark.objects.all()
        allowed_methods = ['get', 'post', 'put', 'patch']
        authorization = Authorization()
        filtering = {
            'tag': ALL,
        }

class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        allowed_methods = ['get', 'post', 'put', 'patch']
        authorization = Authorization()
