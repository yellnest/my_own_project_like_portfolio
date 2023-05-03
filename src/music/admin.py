from django.contrib import admin

from .models import *


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'nick',)
    list_display_links = ('id', 'nick',)
    search_fields = ('nick',)
    prepopulated_fields = {'slug': ('nick',)}


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_title', 'ambiguity', 'slang', 'speech_speed', 'without_text', 'data', 'published')
    search_fields = ('song_title', 'artists')
    list_display_links = ('song_title',)
    list_editable = ('published',)
    list_filter = ('data', 'song_title')
    prepopulated_fields = {'slug': ('song_title',)}
    filter_horizontal = ('artists',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'music', 'username', 'created_date')
    list_display_links = ('id', 'music', 'username')
