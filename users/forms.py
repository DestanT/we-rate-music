from .models import UserProfile
from django import forms


class UserProfileImagesForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("profile_image", "background_image")
