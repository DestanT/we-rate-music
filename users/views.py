from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import UserProfile, Playlist, Club, MembersInClub
from .forms import PlaylistForm


class PlaylistView(View):
    def get(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)
        playlists = Playlist.objects.filter(user=user_profile.user)

        return render(
            request,
            "users/playlists.html",
            {
                "user_profile": user_profile,
                "playlists": playlists,
                "playlist_form": PlaylistForm(),
            },
        )

    def post(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)
        playlists = Playlist.objects.filter(user=user_profile.user)

        playlist_form = PlaylistForm(data=request.POST)

        if playlist_form.is_valid():
            new_playlist = playlist_form.save(commit=False)
            new_playlist.user = user_profile.user
            new_playlist.save()
        else:
            playlist_form = PlaylistForm()

        return render(
            request,
            "users/playlists.html",
            {
                "user_profile": user_profile,
                "playlists": playlists,
                "playlist_form": PlaylistForm(),
            },
        )


class ClubView(View):
    def get(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)
        clubs = MembersInClub.objects.filter(member=user_profile.user)

        return render(
            request,
            "users/clubs.html",
            {"user_profile": user_profile, "clubs": clubs},
        )
