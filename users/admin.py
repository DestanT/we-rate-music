from django.contrib import admin
from .models import UserProfile, Playlist, Songs, Club, MembersInClub


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


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("club_name", "date_created")
    prepopulated_fields = {"slug": ("club_name",)}


@admin.register(MembersInClub)
class UsersInClubAdmin(admin.ModelAdmin):
    list_display = ("date_joined", "club_name", "member")
