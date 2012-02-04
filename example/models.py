"""
Models that descibe a CD library.
"""
from django.db import models
from django.core.urlresolvers import reverse

from bakery.models import BuildableModel

class Album(BuildableModel):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    band = models.ForeignKey('Band')

    slug = models.SlugField()

    detail_views = ['AlbumDetail']

    def get_absolute_url(self):
        return reverse('album-detail', args=[self.slug])

    def __unicode__(self):
        return u'%s - %s' % (self.title, self.band)


class Band(BuildableModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    detail_views = ['BandDetail']

    def get_absolute_url(self):
        return reverse('band-detail', args=[self.slug])

    def __unicode__(self):
        return u'%s' % self.name
