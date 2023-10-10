from .models import UserProfile, Club
from django import forms


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("spotify_username", "profile_image", "background_image")


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ("club_name", "club_image")