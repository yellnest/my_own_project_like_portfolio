from rest_framework.routers import DefaultRouter

from src.music.views import ArtistViewSet, MusicViewSet

router = DefaultRouter()

router.register(r'artist', ArtistViewSet)
router.register(r'music', MusicViewSet)

urlpatterns = router.urls
