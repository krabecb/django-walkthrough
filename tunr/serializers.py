from rest_framework import serializers
from .models import Artist, Song

# Serializers allow us to convert data from QuerySets(Django's data type from ORM)
# to data that can easily be converted to JSON
# Also allows linking from one model to another!

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        # Comes from urls.py
        view_name='song_detail',
        many=True,
        read_only=True
    )

    # Link to artist_detail
    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail'
    )

    class Meta:
       model = Artist
       fields = ('id', 'artist_url', 'photo_url', 'nationality', 'name', 'songs',)

class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    )

    # Link to artist
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = Song
        fields = ('id', 'artist', 'artist_id', 'title', 'album', 'preview_url')