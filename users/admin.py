from django.contrib import admin
from .models import UserProfile, Playlist, Songs


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("playlist_title",)}
    list_display = ("user", "playlist_title", "updated_on")


@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ("song_title", "playlist")
