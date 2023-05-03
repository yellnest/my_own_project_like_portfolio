from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import ArtistSerializer, MusicSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'slug'


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    lookup_field = 'slug'
