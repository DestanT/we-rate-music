from .models import UserProfile, Playlist, Songs
from django import forms


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ("playlist_title",)


class SongsForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = ("song_title",)


class UserProfileImagesForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("profile_image", "background_image")
