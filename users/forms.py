from .models import Playlist
from django import forms


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ("playlist_title",)
