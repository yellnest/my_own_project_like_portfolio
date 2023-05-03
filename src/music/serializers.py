from rest_framework import serializers
from .models import *


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = (
            'id', 'song_title', 'slug', 'comment', 'ambiguity', 'slang', 'speech_speed', 'without_text', 'published',
        )
