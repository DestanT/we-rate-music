from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from .models import UserProfile, Club, ClubInvitation


class UserSettingsForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ("spotify_username", "profile_image", "background_image")


class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ("club_name", "club_image")


class ClubInvitationForm(ModelForm):
    class Meta:
        model = ClubInvitation
        fields = ("user",)