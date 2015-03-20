from django.db import models

class Bookmark(models.Model):
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=128)
    bookmark = models.ManyToManyField(Bookmark)
