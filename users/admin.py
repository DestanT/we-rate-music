from django.contrib import admin
from .models import Playlist, Songs


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("playlist_title",)}
    list_display = ("user", "playlist_title", "updated_on")


@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ("song_title", "playlist")
