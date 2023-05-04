from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.music.views import *

router = DefaultRouter()

router.register(r'artist', ArtistViewSet)
router.register(r'music', MusicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
