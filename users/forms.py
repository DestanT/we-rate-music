from .models import UserProfile
from django import forms


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("spotify_username", "profile_image", "background_image")
