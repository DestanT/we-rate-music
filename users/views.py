from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import UserProfile, Playlist


class PlaylistView(View):
    def get(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)
        playlists = Playlist.objects.filter(user=user_profile.user)

        return render(
            request,
            "users/playlists.html",
            {"user_profile": user_profile, "playlists": playlists},
        )
