from rest_framework import serializers
from .models import *


class ArtistSerializer(serializers.ModelSerializer):
    number_of_songs = serializers.IntegerField(read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'nick', 'slug', 'number_of_songs',)
        # fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    count_avg = serializers.FloatField(read_only=True)

    class Meta:
        model = Music
        fields = (
            'id', 'song_title', 'slug', 'comment', 'ambiguity', 'slang', 'speech_speed', 'without_text', 'count_avg',
            'published',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
