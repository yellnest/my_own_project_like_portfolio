from django.db.models import Count, F
from rest_framework import viewsets, generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail

from .models import *
from .serializers import *
from .permission import IsAdminOrReadOnly


class ArtistViewSet(viewsets.ModelViewSet):
    """Вывод списка артистов
    """
    queryset = Artist.objects.all().annotate(
        number_of_songs=Count('music')
    ).order_by('-pk')

    serializer_class = ArtistSerializer
    lookup_field = 'slug'

    filter_backends = (SearchFilter,)
    filter_fields = ('nick', 'number_of_songs')
    search_fields = ('nick', 'number_of_songs')

    permission_classes = (IsAdminOrReadOnly,)


class MusicViewSet(viewsets.ModelViewSet):
    """Вывод списка песен
    """
    queryset = Music.objects.all().annotate(
        count_avg=(F('ambiguity') + F('slang') + F('speech_speed') + F('without_text')) / 4,
    )

    serializer_class = MusicSerializer
    lookup_field = 'slug'

    filter_backends = (SearchFilter,)
    filter_fields = ('count_avg', 'data')
    search_fields = ('song_title',)

    permission_classes = (IsAdminOrReadOnly,)


class CommentView(generics.ListCreateAPIView):
    """Написание комментария к песне
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        music_slug = self.kwargs['music_slug'].lower()
        music = Music.objects.get(slug=music_slug)
        return Comment.objects.filter(music=music)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class FeedBackView(APIView):
    """Отправление FeedBack на почту
    """
    serializer_class = ContactSerailizer

    def post(self, request, *args, **kwargs):
        serializer_class = ContactSerailizer(data=request.data)
        if serializer_class.is_valid():
            data = serializer_class.validated_data
            name = data.get('name')
            from_email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            send_mail(f'От {name} | {from_email} | {subject} ', message, from_email, ['y0ungada03@gmail.com'])
            return Response({
                'success': 'Удачно отправилось, P.S. Это рил отправляется мне на почту так что не спамь пж'
            })


class RegisterView(generics.GenericAPIView):
    """Регистрация пользователя
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'message': 'Пользователь успешно создан'
        })
