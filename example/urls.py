from django.conf.urls.defaults import patterns, url
from example.views import AlbumDetail, BandDetail

urlpatterns = patterns('',
    url(r'^album/(?P<slug>[-\w+]+)?/$', AlbumDetail.as_view(), name="album-detail"),
    url(r'^band/(?P<slug>[-\w+]+)?/$', BandDetail.as_view(), name="band-detail")
)
