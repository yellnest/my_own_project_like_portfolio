from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from src.music.views import *


urlpatterns = [
    # Основные
    path('', include('config.routers')),

    # Обратная связь
    path('feedback/', FeedBackView.as_view(), name='feedback'),

    # Комменты
    path('comments/', CommentView.as_view()),  # этот url для добавления комментария, а в запросе уже отправляется slug
    path('comments/<slug:music_slug>/', CommentView.as_view()),  # этот url для просмотра комментария по slug

    # JWT токены
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Регистрация
    path('reg/', RegisterView.as_view(), name='feedback'),
]
