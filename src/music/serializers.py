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


class ContactSerailizer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    subject = serializers.CharField()
    message = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer регистрации
    """
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        password2 = validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
