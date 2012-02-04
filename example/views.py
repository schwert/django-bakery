from bakery.views import BuildableDetailView
from models import Album, Band

class AlbumDetail(BuildableDetailView):
    queryset = Album.objects.all() 

class BandDetail(BuildableDetailView):
    queryset = Band.objects.all()
