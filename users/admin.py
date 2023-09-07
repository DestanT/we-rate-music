from django.contrib import admin
from .models import AlbumPlaylist, Songs


@admin.register(AlbumPlaylist)
class AlbumPlaylistAdmin(admin.ModelAdmin):
    list_display = ("created_by", "title", "created_on")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ("name", "artist", "album_playlist")
