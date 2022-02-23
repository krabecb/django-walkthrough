from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Artist, Song

from rest_framework import generics
from .serializers import ArtistSerializer, SongSerializer

# Create your views here.

def artist_list(request):
    artists = Artist.objects.all().values('name', 'nationality', 'photo_url') # only grab some attributes from our database, else we can't serialize it.
    artists_list = list(artists) # convert our artists to a list instead of QuerySet
    return JsonResponse(artists_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.

# def artist_detail(request, pk):
#     artist = Artist.objects.get(id=pk)
#     return HttpResponse(artist)

def song_list(request):
    songs = Song.objects.all().values('artist', 'title', 'album', 'preview_url') # only grab some attributes from our database, else we can't serialize it.
    songs_list = list(songs) # convert our artists to a list instead of QuerySet
    return JsonResponse(songs_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.

def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    return HttpResponse(song)

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer