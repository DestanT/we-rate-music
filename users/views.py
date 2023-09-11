from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Playlist


class PlaylistView(View):
    def get(self, request, *args, **kwargs):
        entries = Playlist.objects.all()

        return render(request, "users/playlists.html", {"playlists": entries})
