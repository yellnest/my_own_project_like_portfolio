from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.music.views import *

router = DefaultRouter()

router.register(r'artist', ArtistViewSet)
router.register(r'music', MusicViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feedback/', FeedBackView.as_view(), name='feedback'),
    path('comments/', CommentView.as_view()),  # этот url для добавления комментария, а в запросе уже отправляется slug
    path('comments/<slug:music_slug>/', CommentView.as_view()),  # этот url для просмотра комментария по slug
]
